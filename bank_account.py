'''Class Definition:

Define a class named BankAccount.
Use the __init__ method to initialize an account_balance attribute. Optionally, accept an initial balance parameter, defaulting to zero.
Encapsulation and Behaviors:

Implement deposit(amount), withdraw(amount), and display_balance() methods.
deposit should add the specified amount to account_balance.
withdraw should deduct the amount from account_balance if funds are sufficient, 
returning True; otherwise, return False and do not alter the balance.
display_balance should print the current balance in a user-friendly format.'''

class BankAccount:
    def __init__(self, account_balance = 0):
        self.__account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        
        return False



    def display_balance(self):
        print(f"Your current balance is: ${self.__account_balance}")


