#! python3
#pw.py - パスワード管理プログラム(脆弱性あり)

passwords = {'email': 'fjieajfiojioaf322ll12k334jF88',
            'blog': 'VmAlvQyKAxiVH5G8v01f1MLZ3dfg',
            'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('使い方: python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print(account + 'のパスワードをクリップボードにコピーしました')
else:
    print(account + 'というアカウント名はありません')