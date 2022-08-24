import re

def restrip(text, chars=r'\s'):
    # print(f'input : "{chars}"')
    strip_regex = re.compile(rf'^[{chars}]*(.*?)[{chars}]*$')
    print(strip_regex.sub(rf'\1', text))


args = ['gorillagorillagorillagorispamgorilla', 'gorillaspam  ', 'spamgorillagorillagorillagorillagorilla', 'gorillaspamgorilla', 'gorillagorillagorillagorillagorillaspamgorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorilla', 'gorillagorillaspamgorillaspam gorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorillagorilla']


for p in range(len(args)):
    restrip(args[p], 'gorilla')