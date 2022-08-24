#! Python3
# PhoneandMail.py - クリップボードから電話番号とメールアドレスを検索する

import pyperclip
import re

#電話番号の正規表現を定義する
phone_regex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?               #市外局番を指定する
                        (\s*|-|\.)?                      #区切り(あってもなくても)
                        (\d{3})                          #3桁の番号
                        (\s*|-|\.)                       #区切り
                        (\d{4})                          #4桁の番号
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?   #内線番号(あってもなくても)
                        )''', re.VERBOSE)

#メールアドレスの正規表現を定義する
email_regex = re.compile(r'''(
                        [\w.%+-]+           #ユーザー名(最低一文字)
                        @
                        [a-zA-Z.-]+           #ドメイン名(最低一文字)
                        (.[a-zA-Z]{2,4})    #トップレベルドメイン
                        )''', re.VERBOSE)

#クリップボード上の文字列を検索する
text = str(pyperclip.paste())
matches = []    #検索結果を格納するリスト
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1]],[groups[3]][groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])
    
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('クリップボードにコピーしました')
    print('\n'.join(matches))
else:
    print('電話番号やメールアドレスは見つかりませんでした')