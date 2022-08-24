""" 
while True:
    age = input('年齢を入力してください:')
    if age.isdecimal():
        break
    print('年齢は数字で入力してください｡')

while True:
    password = input('新しいパスワードを入力してください(英数字のみ):')
    if password.isalnum():
        break
    print('パスワードは英数字で入力してください')
"""

""" 
spam = ['cats', 'rats', 'bats', 'hats',]
bacon = ['My', 'name', 'is', 'Simon']

print('ゴリラ'.join(spam))
print(' '.join(bacon))
print('ABC'.join(bacon))

eggs = 'ABCDE'.join(bacon).split('ABCDE')

print(eggs)
 """

""" 
mint = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Mild Experiment".

Please do not drink it.
Sincerely,
Bob'''

paseli = mint.split('\n')
print('ゴリラ'.join(paseli))
 """


print('Hello'.rjust(10, '*'))
print('Hello'.rjust(20, '_'))
print('Hello world'.rjust(20, '@'))
print('#'* 50 + '\n' +'#' * 50)
print('Hello world'.center(50, '#'))
print('#'* 50 + '\n' +'#' * 50)



