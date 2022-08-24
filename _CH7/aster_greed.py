import re

nongreedy_regex = r'<.*?>'
greedy_regex = r'<.*>'

mo = '<To serve man> for dinner.>'
print(re.search(nongreedy_regex, mo).group())
print(re.search(greedy_regex, mo).group())