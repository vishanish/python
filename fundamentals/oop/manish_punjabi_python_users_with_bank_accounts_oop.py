class BankAccount:
    total_account = 0
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.total_account +=  1
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if not BankAccount.can_withdraw(self.balance, amount):
            self.balance -= 5
            print('Insfufficent Funds: Charging a $5 fee')
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f'Balance: ${self.balance}')
    def yield_interest(self):
        if (self.balance > 0):
            self.yield_interest = self.balance * self.int_rate
        return self
            
    @classmethod
    def total_bank_account(cls):
        print(f'Number of bank accounts {cls.total_account}')

    @staticmethod
    def can_withdraw(balance, amount):
        return (balance - amount) >= 0


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.accounts = {
            "checking" : BankAccount(0.02, 0)
        }
        # self.saving_account = BankAccount(0.4,0)
    def add_account(self, name, int_rate, balance):
        self.accounts[name] = BankAccount(int_rate, balance)
    def deposit(self, amount, name = 'checking'):
        self.accounts[name].deposit(amount)
    # def saving_deposit(self,amount):
    #     self.saving_account.deposit = +amount
    # def make_deposit(self,amount):
    #     self.account_balance.deposit +=amount
    def withdraw(self, amount, name = 'checking'):
        self.accounts[name].withdraw(amount)
    # def saving_withdraw(self,amount):
    #     self.saving_account.withdraw -=amount
    # def make_withdrawal(self,amount):
    #     self.account_balance.withdraw -=amount
    def display_balance(self, name = 'checking'):
        print(f'User:{self.first_name} {self.last_name} {name}', end =' ')
        self.accounts[name].display_account_info()
    # def display_saving_balance(self):
    #     print(f'User:{self.first_name} {self.last_name}: ${self.saving_account.display_account_info}')
    # def display_user_balance(self):
    #     print(f'User:{self.first_name} {self.last_name}: ${self.account_balance.display_account_info}')


guido = User('Guido', 'van Rossum')
guido.deposit(200)
guido.withdraw(100)
guido.display_balance()
guido.add_account('savings', 0.04, 500)
guido.display_balance('savings')