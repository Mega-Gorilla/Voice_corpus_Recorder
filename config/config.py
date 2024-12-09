import os
import sys

class file_path:
    @staticmethod
    def get_base_path():
        """実行ファイルの基準パスを取得"""
        if getattr(sys, 'frozen', False):
            # exe実行時のパス
            return os.path.dirname(sys.executable)
        else:
            # 通常の実行時のパス
            return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @staticmethod
    def get_resource_path():
        """内蔵リソースのパスを取得"""
        if getattr(sys, 'frozen', False):
            # exe実行時は_MEIPASSを使用
            return sys._MEIPASS
        else:
            # 通常実行時はカレントパス
            return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    @property
    def save_folder(self):
        """外部保存用フォルダは実行ファイル位置基準"""
        return os.path.join(self.get_base_path(), 'save')
    
    @property
    def corpus_folder(self):
        """コーパスフォルダは内蔵リソースから取得"""
        return os.path.join(self.get_resource_path(), 'corpus_list')
    
    @property
    def html_folder(self):
        """HTMLフォルダは内蔵リソースから取得"""
        return os.path.join(self.get_resource_path(), 'html')

# シングルトンインスタンスを作成
file_path = file_path()