import re
text='hi,hello world.okay 123-'
match=re.sub(r'[,. ]',r':',text)
print(match)