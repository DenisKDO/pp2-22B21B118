l=['Hi\n','World\n','End\n','salam']
with open('text.txt', 'w') as file:
    for i in l:
        file.write(i)
