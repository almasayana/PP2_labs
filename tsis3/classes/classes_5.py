class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        
a1 = Account("Tihon", 10000)
a1.deposit(300)
a1.withdraw(20000)