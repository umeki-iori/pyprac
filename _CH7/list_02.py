""" spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)
cheese = spam
print(cheese) """

""" spam = list(range(6))
cheese = spam
cheese[1] = 'Hello'
print(spam)
print(cheese) """

""" def eggs(some_parameter):
    some_parameter.append('Hello')


spam = [1, 2, 3]
eggs(spam)
print(spam) """

""" import copy
spam = ['a', 'b', 'c', 'd']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam,cheese) """

""" spam = ['a', 'b', 'c', 'd']
print(spam[int(int('3'*2)/11)])
print(spam[-1])
print(spam[:2]) """

""" bacon = [3.14, 'cat', 11, 'cat', True]

print(bacon.index('cat'))

bacon.append(99)
print(bacon)

bacon.remove('cat')
print(bacon) """

'''
spam = ['a', 'b', 'c', 'd', 'e']
bacon = [list(range(6)), spam]
eggs = [1, 3, 120, 'dog', 'cat', 'cow', spam, 'hoge', bacon]
""" print(spam)
print(bacon)
print(eggs) """

import copy

cheese = copy.copy(bacon)
paseli = copy.deepcopy(bacon)

""" print(cheese)
print(paseli) """

cheese[1] = 'test'
paseli[1] = 'テスト'

print(cheese)
print(paseli)
print(bacon)
'''
