import re
text='a0 abbbb aO ab abbb abab'
match=re.findall(r'\bab*\b',text)
print(match)