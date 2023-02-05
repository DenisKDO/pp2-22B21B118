import random
rannum=random.randint(1,20)
name=input("Hello! What is your name?\n")
print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")
def isright(a,rannum):
    if a==rannum :
        return True
    elif a<rannum:
        print('''Your guess is too low.
Take a guess.''')
    else:
        print('''Your guess is too high.
Take a guess.''')
def game():
    count=0
    while True:
        count+=1
        a=int(input())
        print()
        if isright(a,rannum)==True:
            break
    print(f"Good job, KBTU! You guessed my number in {count} guesses!")
game()



