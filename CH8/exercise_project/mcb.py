#! python3
#multi_clip_boad.py
#usage:
#mcb.py save <keyword> - クリップボードをキーワードに紐づけて保存
#mcb.py <keyword> - キーワードに紐付けられたテキストをクリップボードにコピー
#mcb.py list - 全キーワードを表示

import sys, shelve, pyperclip, os

shelve_path = os.path.join('.', 'shelve_file')
os.makedirs(f'{shelve_path}', exist_ok=True)
mcb_shelf = shelve.open(shelve_path + '\\mcb')


#クリップボードのテキストを保存
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
#deleteコマンドの実装
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] == '--all':
            mcb_shelf.clear()
        elif sys.argv[2] in mcb_shelf:
            del mcb_shelf[sys.argv[2]]
        

elif len(sys.argv) == 2:
    #<keyword>に紐付けられたテキストをクリップボードにコピー
    if sys.argv[1] in mcb_shelf:
        print(mcb_shelf[sys.argv[1]])
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    #すべてのキーワードを表示
    elif sys.argv[1].lower() == 'list':
        print(str(list(mcb_shelf.keys())))
else:
    print('Usage : 引数は "save + <keyword>" or "list" or "<keyword>"')
    
mcb_shelf.close()