import datetime
a=input("YEAR/MONTH/DAY/HOUR/MINUTE/SECOND: ")
b=input("YEAR/MONTH/DAY/HOUR/MINUTE/SECOND: ")
def differences(a,b):
    a=datetime.datetime.strptime(a,'%y/%m/%d/%H/%M/%S')
    b=datetime.datetime.strptime(b,'%y/%m/%d/%H/%M/%S')
    c=a-b
    return c.total_seconds()
print(differences(a,b))
