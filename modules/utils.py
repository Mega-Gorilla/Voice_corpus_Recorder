import inspect
import modules.corpus_dict as corpus_list
import importlib
from config.config import file_path
import re,os
import pykakasi
from pathlib import Path
import glob

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
    htmlファイルをhtml内容文字列で返す
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
    marge_furigana = ""
    for item in furigana:
        marge_furigana+=item['hira']
    furigana = marge_furigana
    
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

def audio_player_if_exists(output_file_path:Path):
    """
    wavファイルをファイルパスから読み込みます
    """
    if output_file_path.exists():
        with output_file_path.open("rb") as f:
            audio_bytes = f.read()
        return audio_bytes
    else:
        return None

def list_directories(path):
    """
    指定されたパス内のフォルダ名のリストを返します。
    パスが存在しない場合は、そのパスにフォルダを作成します。
    
    :param path: フォルダを検索または作成する親ディレクトリのパス
    :return: フォルダ名のリスト
    """
    # 指定されたパスが存在しない場合、ディレクトリを作成
    if not os.path.exists(path):
        os.makedirs(path)
        return []  # 新しく作成したばかりなので、中にフォルダは存在しない

    # 指定されたパスがディレクトリであることを確認
    if not os.path.isdir(path):
        raise ValueError("指定されたパスはディレクトリではありません。")

    # ディレクトリ内の全ての項目をリストアップし、その中からディレクトリのみを選択
    directories = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
    
    return directories

def list_wav_files(path):
    """
    指定されたパス内の.wavファイルのリストを返します。
    指定されたフォルダが存在しない場合はNoneを返します。
    
    :param path: .wavファイルを検索するディレクトリのパス
    :return: .wavファイルのリスト、またはNone
    """
    # 指定されたパスが存在するかどうかを確認
    if not os.path.exists(path) or not os.path.isdir(path):
        return None

    # 指定されたパス内の.wavファイルを検索
    wav_files = glob.glob(os.path.join(path, '*.wav'))
    
    # ファイル名のリストを返す（パスからファイル名のみを抽出）
    return [os.path.basename(file) for file in wav_files]

if __name__ == "__main__":
    test=' シュヴァイツァーは見習うべき人間です。'
    print(auto_add_furigana(test))