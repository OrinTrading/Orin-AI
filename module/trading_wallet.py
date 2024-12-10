class Wallet:
    def __init__(self, initial_funds=0):
        self.balance = initial_funds

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            print("Insufficient balance!")
            return 0

