#Set
#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)
#Duplicates Not allowed, unchangeable, unordered
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Set Items - Data Types
#String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}

#type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)