""" def spam():
    eggs = 99
    bacon()
    print(f'eggs in spam is {eggs}')

def bacon():
    ham = 101
    eggs = 0
    print(f'eggs in bacon is {eggs}')
    print('ham is ' + str(ham))

spam() """

""" def spam():
    print(eggs)

eggs = 42
spam()
print(eggs) """

""" def spam():
    eggs = 'spam local'
    print(eggs)
    print('__________')

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)
    print('__________')

eggs = 'grobal'
bacon()
print(eggs) """

""" def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'bacon'

def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)
ham() """

""" def spam():
    
    # print(eggs)
    eggs = 'spam local'
    print(eggs)

eggs = 'global'
spam() """

""" def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('error:不正な引数です｡')

print('Input any Number.')
print(spam(float(input())))

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1)) """

""" def spam(divide_by):
    return 42 / divide_by

try:
    print(spam(10))
    print(spam(21))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('エラー：不正な引数です｡') """
