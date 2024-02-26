import inspect
import modules.corpus_dict as corpus_list
import importlib
from config import file_path
import re

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
