import re

test_newline_regex = '.*'
text = 'Serve the public trust.\nProtect the innocent.\nUphold the law'
# print(re.search(test_newline_regex, text).group())
print(re.search(test_newline_regex, text, re.DOTALL).group())