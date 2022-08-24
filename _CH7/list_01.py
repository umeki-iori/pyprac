""" spam = ['cat', 'bat', 'rat', 'elephant']

print('The ' + spam[1] + ' ate the ' + spam[0] + '.')

print('The ' + spam[-1] + ' is afraid of the ' + spam[3] + '.') """

""" spam = [str(1), 2, 3] + ['a', 'b', 'c']+ ['A', 'B']

for number in range(0, 8):
    print(number,spam[number], type(spam[number]))
 """

""" cat_names = []
while True:
    print('猫' + str(len(cat_names) + 1) + 'の名前を入力してください' + '(終了するにはEnterだけ押してください')
    name = input()
    if name == '':
        break
    else:
        cat_names = cat_names + [name]
print('猫の名前は次のとおりです｡')
for number, name in enumerate(cat_names):
    # print(str(number) + ':' + name)
    print(f'{number} : {name}') """


""" supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):/
    print('Index' + str(i) + ' in supplies is ' + supplies[i]) """

""" my_pets = ['Zophie', 'Pooka', 'Fat-tail']
print('ペットの名前を入力してください:')
name = input()
if name in my_pets:
    print(name + 'は私のペットです')
else:
    print(name + 'という名前のペットは飼っていません｡') """

""" cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

print(cat) """

""" dog = ['small', 'white', 'silent', 'hoge']
size1, color1, disposition1, name = dog
print(size1)
print(color1)
print(disposition1)
print(name) """

""" spam = 42
spam %= 
print(spam) """

""" spam = ['cat', 'dog', 'bat']
spam.insert(2, 'moose')
print(spam) """

""" spam = ['Ants', 'cats', 'Dogs', 'badgers', 'elephants']
spam.sort(reverse=True,key=str.lower)
print(spam) """