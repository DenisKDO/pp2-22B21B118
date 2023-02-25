import re
text='HelloWorldILoveProgramming'
match=re.findall(r'[A-Z][a-z]+|[A-Z]',text)
print(match)