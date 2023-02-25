import re
text='ab abb abbbbb a00 abb abbb a22 25o'
match=re.findall(r'\bab{2,3}\b',text)
print(match)