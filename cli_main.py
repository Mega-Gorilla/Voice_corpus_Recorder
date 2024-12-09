import streamlit.web.bootstrap as bootstrap
import os
import sys
import tempfile

def get_resource_path():
    """リソースパスの取得"""
    try:
        # PyInstallerの一時ディレクトリを取得
        base_path = sys._MEIPASS
    except Exception:
        # 通常のPython実行時
        base_path = os.path.abspath(".")
    return base_path

def extract_script():
    """実行ファイルから埋め込まれたmain.pyを一時ファイルとして展開"""
    if getattr(sys, 'frozen', False):
        # リソースパスを取得
        base_path = get_resource_path()
        
        # 一時ディレクトリにmain.pyを作成
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, 'main.py')
        
        # main.pyの内容を一時ファイルに書き込み
        main_path = os.path.join(base_path, 'main.py')
        try:
            with open(main_path, 'r', encoding='utf-8') as f:
                content = f.read()
            with open(temp_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"Error extracting script: {e}")
            print(f"Trying to read from: {main_path}")
            return None
            
        return temp_path
    return 'main.py'

if __name__ == "__main__":
    try:
        # スクリプトを一時ファイルとして展開
        script_path = extract_script()
        if script_path is None:
            print("Failed to extract main.py")
            sys.exit(1)
        
        # カレントディレクトリを設定
        base_path = get_resource_path()
        os.chdir(base_path)
        print(f"Working directory: {os.getcwd()}")
        print(f"Script path: {script_path}")
        
        # Streamlit設定
        flag_options = {
        "server.port": 8501,
        "global.developmentMode": False,
        "server.maxUploadSize": 50,  # アップロードサイズ制限を増やす
        "server.maxMessageSize": 50,  # メッセージサイズ制限を増やす
        "server.enableXsrfProtection": False,  # XSRF保護を無効化
        "server.enableCORS": False,  # CORSを無効化
    }

        # 設定をロード
        bootstrap.load_config_options(flag_options=flag_options)
        flag_options["_is_running_with_streamlit"] = True
        
        # mainを実行
        bootstrap.run(
            script_path,
            "streamlit run",
            [],
            flag_options
        )
    except Exception as e:
        print(f"Error during startup: {e}")
        sys.exit(1)