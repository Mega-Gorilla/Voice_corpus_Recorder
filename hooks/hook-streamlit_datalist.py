from PyInstaller.utils.hooks import copy_metadata, collect_data_files
import os
import streamlit_datalist

# メタデータとデータファイルをコピー
datas = copy_metadata('streamlit-datalist')
datas += collect_data_files('streamlit_datalist', include_py_files=True)

# フロントエンドビルドファイルのパスを取得
datalist_path = os.path.dirname(streamlit_datalist.__file__)
frontend_path = os.path.join(datalist_path, 'frontend', 'build')
static_js_path = os.path.join(frontend_path, 'static', 'js')

# フロントエンドファイルを明示的に追加
if os.path.exists(frontend_path):
    datas += [
        (frontend_path, 'streamlit_datalist/frontend/build'),
        (static_js_path, 'streamlit_datalist/frontend/build/static/js'),
    ]

# hiddenimportsの設定
hiddenimports = [
    'streamlit.components.v1',
    'streamlit.components.v1.components'
]