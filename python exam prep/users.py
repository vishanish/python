class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amcount):
        self.balance += amcount
    def withdrawal(self, amount):
        self.withdrawal -=amount
    def display_account_info(self):
        print(self.balance)
    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)

class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def make_transfer(self, first_name, amount):
        self.make_withdrawal(amount)
        first_name.make_deposit(amount)
    def display_user_balance(self):
        print(f'Users:{self.first_name}{self.last_name}Account Balance:{self.account_balance}')