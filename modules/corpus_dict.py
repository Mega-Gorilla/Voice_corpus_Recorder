from config import file_path

# 下記、コードに追加したコーパスをリストで返すコードを記載してください。
# 下記関数は、自動参照されコーパスリストに追加されます。
"""
任意のコーパスを追加する場合、以下のルールで追加してください。

def 任意のコーパス名()->dict:
    任意コーパスを読み込み以下のフォーマットに変換し、returnするコードを記載してください。
    追加した関数は、他のpyファイルでの宣言等は不要です。本corpus_dictに追加した関数は自動的に読み込まれます。
    追加後アプリケーションを起動し、コーパス選択肢に追加されていることを確認してください。
        フォーマット:
        [{name:text}....]
        フォーマット例:
        [{"EMOTION100_001":"えっ嘘でしょ。"},
        {"EMOTION100_002":"シュヴァイツァーは見習うべき人間です。"},
        {"EMOTION100_003":"デーヴィスさんはとても疲れているように見える。"}

GPT-4等で以下のようなプロンプトで自動生成し追加することも可能です。
例：
テキストファイル「JSUT_basic5000.txt」を読み込み変換後のリストに変換するPython関数を提案してください。

#JST_basic5000.txt
BASIC5000_0001:水をマレーシアから買わなくてはならないのです。
BASIC5000_0002:木曜日、停戦会談は、何の進展もないまま終了しました。
BASIC5000_0003:上院議員は私がデータをゆがめたと告発した。
BASIC5000_0004:１週間して、そのニュースは本当になった。

#変換後のリスト
[{"BASIC5000_0001":'水をマレーシアから買わなくてはならないのです。'},
{"BASIC5000_0002":"木曜日、停戦会談は、何の進展もないまま終了しました。"},
{"BASIC5000_0003":"上院議員は私がデータをゆがめたと告発した。"},
{"BASIC5000_0004":"１週間して、そのニュースは本当になった。"}]
"""
    
def JVNV_Corpus()->dict:
    dict_list = []
    with open(f'{file_path.corpus_folder}\JVNV.csv', 'r', encoding='utf-8') as file:
        for line in file:
            # 各行を'|'で分割
            parts = line.strip().split('|')
            if len(parts) == 3:  # 正しいフォーマットの行のみ処理
                # 辞書にキーと値のペアを追加（キーはparts[0], 値はparts[2]）
                new_dict = {parts[0]:parts[2]}
                dict_list.append(new_dict)
    return dict_list

def ITA_Corpus_Emotion()->dict:
    emotion_dict = []
    with open(f'{file_path.corpus_folder}\emotion_transcript_utf8.txt', 'r', encoding='utf-8') as file:
        for line in file:
            # 各行を':'で分割してキーと値を取り出す
            key, value = line.strip().split(':', 1)
            # 値を','でさらに分割して最初の部分のみを取り出す
            value = value.split(',', 1)[0]
            # 辞書にキーと値のペアを追加
            new_dict = {key:value}
            emotion_dict.append(new_dict)
    return emotion_dict

def ITA_Corpus_Recitation()->dict:
    emotion_dict = []
    with open(f'{file_path.corpus_folder}/recitation_transcript_utf8.txt', 'r', encoding='utf-8') as file:
        for line in file:
            # 各行を':'で分割してキーと値を取り出す
            key, value = line.strip().split(':', 1)
            # 値を','でさらに分割して最初の部分のみを取り出す
            value = value.split(',', 1)[0]
            # 辞書にキーと値のペアを追加
            new_dict = {key:value}
            emotion_dict.append(new_dict)
    return emotion_dict

def JSUT_Corpus():
    converted_list = []
    with open(f'{file_path.corpus_folder}/JSUT_basic5000.txt', 'r', encoding='utf-8') as file:
        for line in file:
            # コロンでIDとテキストを分割
            parts = line.strip().split(':', 1)
            if len(parts) == 2:
                # 分割したデータを辞書に格納し、リストに追加
                converted_list.append({parts[0]: parts[1]})
    return converted_list

def JVS_Corpus_voiceactress100():
    converted_list = []
    with open(f'{file_path.corpus_folder}/voiceactress100_transcript_utf8.txt', 'r', encoding='utf-8') as file:
        for line in file:
            # コロンでIDとテキストを分割
            parts = line.strip().split(':', 1)
            if len(parts) == 2:
                # 分割したデータを辞書に格納し、リストに追加
                converted_list.append({parts[0]: parts[1]})
    return converted_list

if __name__ == "__main__":
    print(ITA_Corpus_Recitation())