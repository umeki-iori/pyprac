import re
from tkinter.font import names

'''
names_regex = re.compile(r'Agent \w+')
text = 'Agent Alice gave the secret documents to Agent Bob.'
print(names_regex.sub('CENSORED', text))
'''

agent_names_regex = re.compile(r'Agent (\w)(\w?)(\w*)')
text = 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
print(agent_names_regex.sub(r'\1hoge', text))

