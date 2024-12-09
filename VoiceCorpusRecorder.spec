# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files, collect_submodules
import os
import streamlit_webrtc
import streamlit_datalist

block_cipher = None

# パスの設定
current_dir = os.getcwd()

a = Analysis(
    ['cli_main.py'],
    pathex=[current_dir],
    binaries=[],
    datas=[
        (os.path.join(current_dir, 'main.py'), '.'),
        (os.path.join(current_dir, 'config'), 'config'),
        (os.path.join(current_dir, 'modules'), 'modules'),
        (os.path.join(current_dir, 'html'), 'html'),
        (os.path.join(current_dir, 'corpus_list'), 'corpus_list'),
        # saveフォルダは実行時に作成されるので、空フォルダとして含める
        (os.path.join(current_dir, 'save'), 'save')
    ] + collect_data_files('streamlit_datalist') + collect_data_files('streamlit_webrtc'),
    hiddenimports=[
        'streamlit',
        'streamlit.web.cli',
        'streamlit.runtime.scriptrunner.magic_funcs',
        'streamlit_webrtc',
        'streamlit_datalist',
        'pydub',
        'pykakasi',
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
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)