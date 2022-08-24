#! python3
# bulletPointAdder.py
#クリップボードのテキストの各行に点を打って､Wikipediaの箇条書きにする

import pyperclip
targettext = pyperclip.paste()

print(targettext)
lines = targettext.split('\n')
for i in range(len(lines)):
    lines[i] = ['* ' + lines[i]]

print(lines)
targettext = '\n'.join(lines)
pyperclip.copy(targettext)