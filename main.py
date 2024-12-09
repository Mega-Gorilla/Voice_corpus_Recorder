from modules.corpus_dict import *
from modules.utils import *
from modules.webrtc import WebRTCRecord
from config.config import file_path
import streamlit as st
import time
from pathlib import Path

def main():
    st.set_page_config(page_title='Voice Corpus Recorder',
                       menu_items={
                           'Get Help':'https://github.com/Mega-Gorilla/Voice_corpus_Recorder',
                           'Report a bug':'https://github.com/Mega-Gorilla/Voice_corpus_Recorder/issues',
                           'About':'''### Voice Corpus Reader v1.0

Created by 猩々 博士
'''
                       },
                       page_icon='🎙')
    
    corpus_list = get_function_list('modules.corpus_dict')
    select_voiceCorpus = st.selectbox('1.ボイスコーパスの選択',corpus_list)
    corpus_dict = execute_function('modules.corpus_dict',select_voiceCorpus)
    
    current_time = time.time()
    folder_list = list_directories(file_path.save_folder)
    if len(folder_list) == 0:
        folder_list.insert(0,f"{time.strftime('%Y-%m-%d', time.localtime(current_time))} - {select_voiceCorpus}")
    save_folder = st.selectbox("2.保存フォルダの選択", options=folder_list, index=0)
    corpus_num = st.number_input('3.選択されているコーパス番号',max_value=len(corpus_dict),min_value=1)

    #コーパス達成度を表示
    list_wav = list_wav_files(f"{file_path.save_folder}/{save_folder}")
    if list_wav!=None:
        done_percent = int((len(list_wav)/len(corpus_dict))*100)
        wav_len = len(list_wav)
    else:
        done_percent=0
        wav_len=0
    st.progress(done_percent,text=F"達成度 [{done_percent}% {wav_len}/{len(corpus_dict)}]")
    
    # コーパスに基づいたテキストの表示
    corpus_key = None
    for key,value in corpus_dict[corpus_num-1].items():
        value = auto_add_furigana(value) # フリガナを自動追加します。
        value = value.replace('。', '。<BR>')
        value = value.replace('、', '、<BR>')
        value = value.replace('\n', '<BR>')
        corpus_text = read_html('corpus_text')
        corpus_text = corpus_text.format(key=key,value=value)
        corpus_key = key

        st.markdown(f'{corpus_text}',unsafe_allow_html=True)
    
    # 録音機能表示
    wertc_record = WebRTCRecord()
    wertc_record.recording(corpus_key,f"{file_path.save_folder}/{save_folder}")

    # 録音済みの場合、音声データを表示
    audio = audio_player_if_exists(Path(f"{file_path.save_folder}/{save_folder}/{corpus_key}.wav"))
    if audio !=None:
        st.audio(audio)

    # 設定の表示
    with st.expander("録音設定"):
        if "gain_value" not in st.session_state:
            st.session_state.gain_value = 1.0
        st.session_state.gain_value = st.slider("ゲイン調整", min_value=0.1, max_value=2.0, value=st.session_state.gain_value, step=0.1)

if __name__ == "__main__":
    main()