#! python3
#mcb.pyw - クリップボードのテキストを保存/復元
#Usage:
#py.exe mcb.pyw save <keyword> - クリップボードをキーワードに紐づけて保存
#py.exe mcb.pyw <keyword> - キーワードに紐付けられたテキストをクリップボードにコピー
#py.exe mcb.pyw list - 全キーワードをクリップボードにコピー

import shelve, pyperclip, sys

mcb_shelf = shelve.open('shelve\mcb')

# ToDo : クリップボードの内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] == '--All':
        mcb_shelf.clear()
    else:    
        del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
# ToDo : キーワード一覧と,内容の読み込み
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
        print(list(mcb_shelf.keys()))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

        
mcb_shelf.close()
