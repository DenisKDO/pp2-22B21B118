import itertools
def allper():
    a=input()
    per=itertools.permutations(a)
    for i in per:
        print(i)
allper()

