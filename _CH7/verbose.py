import re

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              #3桁の市外局番(()が付いていても良い)
    (\s|-|\.)?                      #区切り(スペースかハイフンかドット)
    \d{3}                           #3桁の市内局番
    (\s|-|\.)                       #区切り
    \d{4}                           #4桁の番号
    (\s*(ext|x|ext.)\s*\d{2,5})?    #2～5桁の内線番号
    )''', re.VERBOSE | re.I | re.DOTALL)

phone_number = r'(001)-447.8842 EXt#                   3287'

print(phone_regex.search(phone_number).group())