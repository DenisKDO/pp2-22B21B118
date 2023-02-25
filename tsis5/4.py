import re
text='Hello Hi world INCREDIBLE'
match=re.findall(r'[A-Z][a-z]+',text)
print(match)