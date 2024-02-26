# 下記、コードに追加したコーパスをリストで返すコードを記載してください。
# 下記関数は、自動参照されコーパスリストに追加されます。
"""
フォーマット:
[{name:text}....]
フォーマット例:
[{"EMOTION100_001":"えっ嘘でしょ。"},
{"EMOTION100_002":"シュヴァイツァーは見習うべき人間です。"},
{"EMOTION100_003":"デーヴィスさんはとても疲れているように見える。"}
"""
    
def JVNV_Corpus()->dict:

    dict_list = []
    with open('corpus_list\JVNV.csv', 'r', encoding='utf-8') as file:
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
    with open('corpus_list\emotion_transcript_utf8.txt', 'r', encoding='utf-8') as file:
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
    with open('corpus_list/recitation_transcript_utf8.txt', 'r', encoding='utf-8') as file:
        for line in file:
            # 各行を':'で分割してキーと値を取り出す
            key, value = line.strip().split(':', 1)
            # 値を','でさらに分割して最初の部分のみを取り出す
            value = value.split(',', 1)[0]
            # 辞書にキーと値のペアを追加
            new_dict = {key:value}
            emotion_dict.append(new_dict)
    return emotion_dict

if __name__ == "__main__":
    print(ITA_Corpus_Recitation())