import inspect
import modules.corpus_dict as corpus_list
import importlib
from config import file_path
import re
import pykakasi

def get_function_list(pyfile_Name:str):
    """
    関数一覧を取得し、リストで返す
    """
    # corpus_dict モジュールを動的にインポートする
    corpus_dict_module = importlib.import_module(pyfile_Name)
    
    # corpus_dict モジュール内の関数一覧を取得する
    functions = [name for name, obj in inspect.getmembers(corpus_dict_module) if inspect.isfunction(obj)]
    
    return functions

def execute_function(pyfile_Name:str,function_name: str) -> dict:
    '''
    指定された文字列関数名を実行する
    '''
    # Dynamically import the corpus_dict module
    corpus_dict_module = importlib.import_module(pyfile_Name)
    
    # Access the specified function by name
    corpus_function = getattr(corpus_dict_module, function_name)
    
    # Execute the function and capture its return value
    result_dict = corpus_function()
    
    # Return the result
    return result_dict

def read_html(html_name:str) -> str:
    """
    htmlファイルを文字列で返す
    """
    # ファイルを読み込む
    with open(f'{file_path.html_folder}/{html_name}.html', 'r', encoding='utf-8') as file:
        content = file.read()

    # //* *// で囲まれた文字列を {key} に置換
    content = re.sub(r'/\*\*(.*?)\*\*/', r'{\1}', content)
    content = content.replace('{','{{')
    content = content.replace('}','}}')
    content = content.replace('//*','{')
    content = content.replace('*//','}')
    return content

def kanji_to_furigana(text:str) -> str:
    kks = pykakasi.kakasi()
    furigana = kks.convert(text)
    furigana = furigana[0]['hira']
    
    #textにひらがなが含まれている場合
    kanji_pattern = re.compile(r'[一-龥]')
    no_kanji_text = re.sub(kanji_pattern, '', text)
    if len(no_kanji_text)!=0:
        for char in no_kanji_text:
            furigana = furigana.replace(char,"")
    return furigana

def auto_add_furigana(text:str) -> str:
    '''
    文字列から漢字を認識しフリガナを自動でふります
    '''
    kanji_group_pattern = re.compile(r'[一-龥]+')
    html_result = ""
    
    start = 0
    for match in kanji_group_pattern.finditer(text):
        # 漢字グループの前のテキストを追加
        html_result += text[start:match.start()]
        # 連続する漢字に続く1文字を含めてフリガナを問い合わせ
        kanji_group_with_next_char = text[match.start():match.end() + 1] 
        
        furigana = kanji_to_furigana(kanji_group_with_next_char)
        # HTMLの<ruby>タグを使用してフリガナを振る
        kanji_group = match.group()
        html_result += f"<ruby>{kanji_group}<rt>{furigana}</rt></ruby>"
        start = match.end() -1
        # 続く1文字が漢字の一部であった場合、それを結果に含める
        if len(kanji_group_with_next_char) > len(kanji_group):
            start += 1
     # 最後の漢字グループ以降のテキストを追加
    html_result += text[start:]
            
    return html_result

if __name__ == "__main__":
    test=' シュヴァイツァーは見習うべき人間です。'
    print(auto_add_furigana(test))