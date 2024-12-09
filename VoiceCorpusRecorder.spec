# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files, collect_submodules, copy_metadata
import os
import streamlit_webrtc
import streamlit_datalist
import pykakasi

block_cipher = None

# パスの設定
current_dir = os.getcwd()
webrtc_path = os.path.dirname(streamlit_webrtc.__file__)
datalist_path = os.path.dirname(streamlit_datalist.__file__)
pykakasi_path = os.path.dirname(pykakasi.__file__)

# フロントエンドパスの設定
webrtc_frontend_path = os.path.join(webrtc_path, 'frontend', 'build')
datalist_frontend_path = os.path.join(datalist_path, 'frontend', 'build')

# 必要なメタデータとデータファイルを収集
all_datas = [
    (os.path.join(current_dir, 'main.py'), '.'),
    (os.path.join(current_dir, 'config'), 'config'),
    (os.path.join(current_dir, 'modules'), 'modules'),
    (os.path.join(current_dir, 'html'), 'html'),
    (os.path.join(current_dir, 'corpus_list'), 'corpus_list'),
    (os.path.join(current_dir, 'save'), 'save'),
    # webrtc関連ファイル
    (webrtc_frontend_path, 'streamlit_webrtc/frontend/build'),
    (os.path.join(webrtc_frontend_path, 'static', 'js'), 'streamlit_webrtc/frontend/build/static/js'),
    # datalist関連ファイル
    (datalist_frontend_path, 'streamlit_datalist/frontend/build'),
    (os.path.join(datalist_frontend_path, 'static', 'js'), 'streamlit_datalist/frontend/build/static/js'),
    # pykakasi データファイル
    (os.path.join(pykakasi_path, 'data'), 'pykakasi/data')
]

# メタデータを追加
for package in ['streamlit', 'streamlit-webrtc', 'streamlit-datalist', 'pykakasi']:
    all_datas.extend(copy_metadata(package))

# 追加のデータファイルを収集
all_datas.extend(collect_data_files('streamlit_datalist'))
all_datas.extend(collect_data_files('streamlit_webrtc'))
all_datas.extend(collect_data_files('pykakasi'))

a = Analysis(
    ['cli_main.py'],
    pathex=[current_dir],
    binaries=[],
    datas=all_datas,
    hiddenimports=[
        'streamlit',
        'streamlit.web.cli',
        'streamlit.runtime.scriptrunner.magic_funcs',
        'streamlit.runtime',
        'streamlit.web',
        'streamlit.elements',
        'streamlit.components.v1',
        'streamlit_webrtc',
        'streamlit_datalist',
        'pydub',
        'pykakasi',
        'pykakasi.kakasi',
        'altair',
        'importlib_metadata',
        'importlib.metadata',
        'streamlit.bootstrap',
        'streamlit.web.bootstrap',
        'av',
        'aiortc',
        'config.config'
    ],
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='VoiceCorpusRecorder',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)