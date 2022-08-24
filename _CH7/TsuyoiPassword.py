import re

pass_regex = re.compile(r'''(
                        ^
                        (?=.*[a-zA-Z0-9]{8,})
                        (?=.*[a-z]+)
                        (?=.*[A-Z]+)
                        (?=.*\d+)
                        .*$
                        )''', re.VERBOSE)
# print(pass_regex)
password = 'Hogehog8'

passwords = ['a2cdeaRa', 'abcdeA1', '', '        ',
                 'abcdefgh', 'abcdefgA', 'abcdefg1',
                 'ABCDEFGH', 'ABCDEFGa', 'ABCDEFG1',
                 '12345678', '1234567a', '1234567A']

print(pass_regex.search(password))
# print(pass_regex.search(password))
for p in range(len(passwords)):
    # print(pass_regex.search(passwords[p]))
    if pass_regex.search(passwords[p]) == None:
        print(str(passwords[p].ljust(12)) + ' は脆弱なパスワードです')
    else:
        print(str(passwords[p].ljust(12)) + ' は強固です')
