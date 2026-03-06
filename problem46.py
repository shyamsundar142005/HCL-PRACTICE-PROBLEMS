class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):   # getter method
        return self.__balance

acc = BankAccount(1000)

acc.deposit(500)
acc.withdraw(200)

print("Current Balance:", acc.get_balance())