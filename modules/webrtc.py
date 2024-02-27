import queue
from pathlib import Path
import pydub
import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer
import os,stat

# 本スクリプトは、「https://github.com/yagays/toji/blob/main/toji/webrtc.py」を参照しています。
class WebRTCRecord:
    def __init__(self):
        self.webrtc_ctx = webrtc_streamer(
            key="sendonly-audio",
            mode=WebRtcMode.SENDONLY,
            audio_receiver_size=256,
            rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
            media_stream_constraints={
                "audio": True,
                "video": False,
            },
        )

        if "audio_buffer" not in st.session_state:
            st.session_state["audio_buffer"] = pydub.AudioSegment.empty()

    def recording(self, output_wav_name:str,wav_file_path:Path):
        status_box = st.empty()

        while True:
            if self.webrtc_ctx.audio_receiver:
                try:
                    audio_frames = self.webrtc_ctx.audio_receiver.get_frames(timeout=1)
                except queue.Empty:
                    status_box.warning("No frame arrived.")
                    continue

                status_box.info("Now Recording...")

                sound_chunk = pydub.AudioSegment.empty()
                for audio_frame in audio_frames:
                    sound = pydub.AudioSegment(
                        data=audio_frame.to_ndarray().tobytes(),
                        sample_width=audio_frame.format.bytes,
                        frame_rate=audio_frame.sample_rate,
                        channels=len(audio_frame.layout.channels),
                    )
                    sound_chunk += sound

                if len(sound_chunk) > 0:
                    st.session_state["audio_buffer"] += sound_chunk
            else:
                break

        audio_buffer = st.session_state["audio_buffer"]

        if not self.webrtc_ctx.state.playing and len(audio_buffer) > 0:
            status_box.success("Finish Recording")
            try:
                if not os.path.exists(wav_file_path):
                    os.makedirs(wav_file_path)
                    os.chmod(path=wav_file_path, mode=stat.S_IWRITE)
                audio_buffer.export(f'{wav_file_path}/{output_wav_name}.wav', format="wav")
            except BaseException:
                st.error("Error while Writing wav to disk")

            # Reset
            st.session_state["audio_buffer"] = pydub.AudioSegment.empty()
