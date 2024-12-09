from PyInstaller.utils.hooks import collect_data_files, copy_metadata

# メタデータをコピー
datas = copy_metadata('streamlit')
datas += collect_data_files('streamlit', include_py_files=True)

# 追加の依存関係のメタデータもコピー
datas += copy_metadata('altair')
datas += copy_metadata('numpy')
datas += copy_metadata('pandas')
datas += copy_metadata('pillow')
datas += copy_metadata('pyarrow')

# hiddenimportsの設定
hiddenimports = [
    'streamlit.runtime.scriptrunner.magic_funcs',
    'streamlit.runtime',
    'streamlit.web',
    'streamlit.elements',
    'importlib.metadata',
]