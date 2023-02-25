import re
text='helloWorldILoveProgramming'
match=re.sub(r'(?=[A-Z])',r'_',text).lower()
print(match)