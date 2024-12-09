import queue
from pathlib import Path
import pydub
import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer
import os
import stat

class WebRTCRecord:
    def __init__(self):
        # ICE Serversの設定を追加
        rtc_configuration = {
            "iceServers": [
                {"urls": ["stun:stun.l.google.com:19302"]}
            ],
            "iceTransportPolicy": "all"
        }

        self.webrtc_ctx = webrtc_streamer(
            key="sendonly-audio",
            mode=WebRtcMode.SENDONLY,
            audio_receiver_size=256,
            rtc_configuration=rtc_configuration,
            media_stream_constraints={
                "audio": {
                    "echoCancellation": True,
                    "noiseSuppression": True,
                    "autoGainControl": True
                },
                "video": False,
            },
            async_processing=True,
        )

        if "audio_buffer" not in st.session_state:
            st.session_state["audio_buffer"] = pydub.AudioSegment.empty()

    def recording(self, output_wav_name: str, wav_file_path: Path):
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
                    try:
                        sound = pydub.AudioSegment(
                            data=audio_frame.to_ndarray().tobytes(),
                            sample_width=audio_frame.format.bytes,
                            frame_rate=audio_frame.sample_rate,
                            channels=len(audio_frame.layout.channels),
                        )
                        sound_chunk += sound
                    except Exception as e:
                        status_box.error(f"Error processing audio frame: {e}")
                        continue

                if len(sound_chunk) > 0:
                    st.session_state["audio_buffer"] += sound_chunk
            else:
                break

        audio_buffer = st.session_state["audio_buffer"]
        if not self.webrtc_ctx.state.playing and len(audio_buffer) > 0:
            status_box.success("Finish Recording")
            try:
                if not os.path.exists(wav_file_path):
                    os.makedirs(wav_file_path, exist_ok=True)
                    os.chmod(path=wav_file_path, mode=stat.S_IWRITE)
                
                output_path = os.path.join(wav_file_path, f"{output_wav_name}.wav")
                audio_buffer.export(output_path, format="wav")
                
                # 録音完了後にバッファをクリア
                st.session_state["audio_buffer"] = pydub.AudioSegment.empty()
                
            except Exception as e:
                st.error(f"Error while Writing wav to disk: {e}")
            
            # ファイルが正常に保存されたか確認
            if os.path.exists(output_path):
                status_box.success(f"Recording saved to: {output_path}")
            else:
                status_box.error("Failed to save recording")