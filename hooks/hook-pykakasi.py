from PyInstaller.utils.hooks import copy_metadata, collect_data_files

# メタデータとデータファイルをコピー
datas = copy_metadata('pykakasi')
datas += collect_data_files('pykakasi', include_py_files=True)

# 特にdataディレクトリを明示的に含める
hiddenimports = ['pykakasi.kakasi']