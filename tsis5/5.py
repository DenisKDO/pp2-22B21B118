import re
text='a00kfsldb a111 HELLO b a--keyb'
match=re.findall(r'a.+?b',text)
print(match)