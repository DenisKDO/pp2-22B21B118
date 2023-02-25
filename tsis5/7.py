import re
text='snake_case_example'
match=re.split(r'_',text)
match=match[0]+''.join(map(str.capitalize,match[1:]))
print(match)