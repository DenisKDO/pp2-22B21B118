import re
text='text_hello_HELLO_wOrL_d_good'
match=re.findall(r"[a-z]+(?=_)|[a-z]+(?=\Z)",text)
print(match)