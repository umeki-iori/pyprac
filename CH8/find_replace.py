#! python3
#find_replace.py - 特定ディレクトリ内のテキストファイルをすべて開いてユーザーが指定した正規表現にマッチする行を検索し､結果を画面に表示する｡

import os, re, argparse

#引数の定義
parser = argparse.ArgumentParser(description='add source directory and regular expression pattern')
parser.add_argument('arg1', type=str, help='対象ディレクトリを指定する')
parser.add_argument('arg2', type=str,  help='検索したい正規表現を指定する')

args = parser.parse_args()

#正規表現を定義
find_regex = re.compile(args.arg1)

#ファイルを読み込んで内容を検索する
for filename in os.listdir(args.arg1):
    if not filename.lower().endswith('.txt'):
        #対象ファイルの読み込み方に別のメソッドを｡