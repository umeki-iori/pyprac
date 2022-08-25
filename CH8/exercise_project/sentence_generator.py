#! python3
# sentence_generator.py - 特定の品詞を書き換える作文ジェネレーター
# -*- coding: utf-8 -*-

import os, re


#検索対象のワードを定義
text_regex = re.compile(r'(<形容詞>|<名詞>|<動詞>)')

#Sourceファイルを読み込む
source_text = open(os.path.join('.', 'TextFile', 'source.txt'), 'r', encoding='utf-8')
read_text = source_text.read()
source_text.close()

#source_text内の文字列を検索する
print(f'読み込まれたファイル : {read_text}')
while True:
    mo = text_regex.search(read_text)
    if not mo:
        break
    else:
        replace_word = input(f'{mo.group(1)}を置換する言葉を入力してください : ')
        read_text = read_text.replace(mo.group(1), replace_word, 1)
        
print(read_text)        

#置換されたテキストを別ファイルとして出力
out_text = open(os.path.join('.', 'TextFile', 'generated.txt'), 'w', encoding='utf-8')
out_text.write(read_text)
out_text.close()
