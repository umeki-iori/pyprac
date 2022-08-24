""" spam = ['cats', 'dogs', 'moose']
bacon = ['cats', 'moose', 'dogs']
eggs = ['cats', 'dogs', 'moose']

print(spam == bacon)
print(spam == eggs) """

""" eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham) """


""" 
birthday = {'Alice': '4/1', 'Bob': '12/12', 'Carol': '4/4'}

while True:
    name = input('名前を入力してください(終了する場合はEnterだけ押してください)')
    if name == '':
        break

    if name in birthday:
        print(name + 'の誕生日は' + birthday[name])
    else:
        print(name + 'の誕生日は未登録です')
        bday = input('誕生日を入力してください')
        birthday[name] = bday
        print('誕生日データベースを更新しました')
 """


''' 
spam = {'color': 'red', 'age': '8', 'sise': 'fat', 'disposition': 'loud', 'name': 'Zopie'}
""" for v in spam.items():
    print(v) """

eggs = list(spam.items())
for k, v in spam.items():
    print('Key: ' + k + ', value: ' + str(v))

print('name' in spam.keys())
'''

""" picnic_items = {'alles': '5', 'cups': '2'}
print('I am bringing ' + str(picnic_items.get('cups', 0)))
print('I am bringing ' + str(picnic_items.get('eggs', 0))) """

""" 
spam = {'name': 'pooka', 'age': 5}
spam.setdefault('color', 'black')
spam.setdefault('weight', 60.5)
spam.setdefault('color', 'white')
spam.setdefault('Null', None)
print(spam)
print(type(spam['weight']))
print(type(spam['Null']))
"""


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] += 1

import pprint
pprint.pprint(count)
