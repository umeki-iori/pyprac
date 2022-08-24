import random

messages = ['たしかにそうだ',
    '間違いなくそうだ',
    'はい',
    'なんとも｡もういちどやってみて',
    '後でもう一度聞いてみて',
    '集中してもう一度きいみて',
    '私の答えはノーです',
    '見通しはそれほど良くない',
    'とても疑わしい']

""" messages = ['たしかにそうだ',
    '間違いなくそうだ',
    'はい',
    'なんとも｡もういちどやってみて',
    '後でもう一度聞いてみて',
    '集中してもう一度きいみて',] """

for i in range(100):
    generated = random.randint(0, len(messages) - 1)

    print(f"{generated} : {messages[generated]}")