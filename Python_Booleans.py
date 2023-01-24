#Boolean Values
#1
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#2
print(10 > 9)
print(10 == 9)
print(10 < 9)
#Evaluate Values and Variables. Evaluate a string and a number:
#1
print(bool("Hello"))
print(bool(15))
#2
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
#Most values are true: the following return true:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#Some values are false:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#Functions can return boolean
def myFunction() :
  return True

print(myFunction())
#Check if an object is an int:
x = 200
print(isinstance(x, int))
