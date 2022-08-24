import os

#os.makedirs(r'.\testfolder')
hello_file = open(r'.\testfolder\hoge.txt')

hello_content = hello_file.read()


hoge_file = open(r'./testfolder\hoge.txt')
print(hoge_file.readlines())