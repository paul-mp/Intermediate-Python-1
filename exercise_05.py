#Utilized these links:
#https://www.geeksforgeeks.org/__init__-in-python/ - for __init__
#https://www.w3schools.com/python/python_classes.asp - classes
#https://realpython.com/python-string-formatting/ - formatting

class BankAccount:
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance is ${self.balance}."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrew ${amount}. New balance is ${self.balance}."

    def get_balance(self):
        return f"{self.account_name} has a balance of ${self.balance}"

account = BankAccount("John Doe", 200)

print(account.deposit(100))
print(account.withdraw(229.84))
print(account.get_balance())
# I tried getting the final amount just like on the example. 