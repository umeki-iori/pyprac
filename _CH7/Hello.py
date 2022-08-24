""" name = input('あなたの名前はなんですか?\n')
print('こんにちは､"' + name + '" さん') """
import math


""" x = input('x = ')
# y = input('y = ')

x = float(x)
y = math.pi

print('x^2 * pi = {}'.format(pow(x,2)*y)) """

"""x = 'Alice' 
y = 6

y = str(y)

print(x + y)
print(x * 5) """

""" print('Hello World!')
print('What is your name?')
my_name = input()
print('It is good to meet you, ' + my_name)
print('The length of your name is : ' + str(len(my_name)))
# print(len(my_name))
print('What is your age?')
my_age = input()
print('You will be ' + str(int(my_age) + 1) + ' in a year.')
"""

""" w = 2.1
x = 0.5
y = -0.5
z = 1.5

print(round(w))
print(round(x))
print(round(y))
print(round(z)) """

""" print(42 == 42)
print(42 == 42.1)
print(2 != 3)
print(2 != 2) """


""" print('Input your name.')
my_name = input()
if my_name == 'Mary':
    print('Hello Mary')
    name_verification = True
else:
    print('Name does not match.')
    name_verification = False
#end

if name_verification == True:
    print('Input password')
    my_pass = input()
    if my_pass == 'Swordfish':
        print('Your password is verified.')
    else:
        print('Password does not match.')"""

print('Input your name.')
name = input()
if name == 'Alice':
    print('やあ､Alice｡')
    name_verification = True
else:
    name_verification = False
    print('Input your age.')
    age = input()
    age = int(age)

if name_verification != True:
    if age < 12:
        print('Aliceじゃないね､お嬢ちゃん｡')
    elif age > 2000:
        print('Aliceはお前のような不死身ではない､吸血鬼め｡')
    elif age > 100:
        print('Aliceじゃないね､お婆ちゃん｡')

