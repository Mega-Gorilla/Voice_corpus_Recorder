import streamlit as st
import inspect
import modules.corpus_dict as corpus_list
import importlib

def get_function_list(pyfile_Name:str):
    """
    関数一覧を取得し、リストで返す
    """
    # corpus_dict モジュールを動的にインポートする
    corpus_dict_module = importlib.import_module(pyfile_Name)
    
    # corpus_dict モジュール内の関数一覧を取得する
    functions = [name for name, obj in inspect.getmembers(corpus_dict_module) if inspect.isfunction(obj)]
    
    return functions
    # Streamlit のセレクトボックスで関数一覧を表示する
    select_box = st.selectbox('Select Voice Corpus', functions)
    return select_box

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