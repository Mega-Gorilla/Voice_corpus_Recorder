from modules.corpus_dict import *
from modules.utils import *
import streamlit as st
import time

def main():
    corpus_list = get_function_list('modules.corpus_dict')
    select_voiceCorpus = st.selectbox('1.ボイスコーパスの選択',corpus_list)
    corpus_dict = execute_function('modules.corpus_dict',select_voiceCorpus)
    
    current_time = time.time()
    save_folder = st.text_input('2.保存フォルダ名の設定',value=f"{time.strftime('%Y-%m-%d', time.localtime(current_time))} - name - {select_voiceCorpus}")
    corpus_num = st.number_input('3.選択されているコーパス番号',max_value=len(corpus_dict),min_value=1)
    
    for key,value in corpus_dict[corpus_num-1].items():
        value = value.replace('。', '。<BR>')
        value = value.replace('、', '、<BR>')
        value = value.replace('\n', '<BR>')
        corpus_text = read_html('corpus_text')
        corpus_text = corpus_text.format(key=key,value=value)

        st.markdown(f'{corpus_text}',unsafe_allow_html=True)

if __name__ == "__main__":
    main()