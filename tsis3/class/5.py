class Account:
    def __init__(self,owner,balance): 
        self.owner=owner
        self.balance=balance
        self.dep=0
    def deposit(self, howmuch):
        if howmuch>self.balance:
            print(f"{self.owner}, you have insufficient funds")
        else: 
            self.balance=self.balance-howmuch
            self.dep=self.dep+howmuch
            print(f"Your deposit replenished on {howmuch}\n{self.owner}, your certain balance: {self.balance}")
    def withdraw(self,howmuch):
        if howmuch>self.balance:
            print(f"{self.owner}, you have insufficient funds")
        else:
            self.balance=self.balance-howmuch
            print(f"{self.owner}, your certain balance: {self.balance}")

print("Creating bank account")
a=input("Enter your name: ")
b=int(input("Enter your balance: "))
acc=Account(a,b)
while True:
    c=input("What do you want to do: (Deposit) (Withdraw) (Exit): ")
    if c=='Deposit':
        d=int(input(f"{acc.owner}, how much do you want to top up your deposit? "))
        acc.deposit(d)
    elif c=='Withdraw':
        d=int(input(f"{acc.owner}, how much do you want to withdraw? "))
        acc.withdraw(d)
    elif c=='Exit':
        print(f'{acc.owner}, have a nice day, goodbye')
        break
    else:
        print('''You have only 3 options:
(Deposit)
(Withdraw)
(Exit)''')


        