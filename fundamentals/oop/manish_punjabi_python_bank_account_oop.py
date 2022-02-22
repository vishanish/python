class BankAccount:
    total_account = 0
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.total_account +=  1
    def desposit(self, amount):
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

guido = BankAccount(0.01, 1000)
manish = BankAccount(0.01, 500)

guido.desposit(300).desposit(500).desposit(500).withdraw(300).yield_interest()
manish.desposit(300).desposit(700).withdraw(100).withdraw(400).withdraw(200).withdraw(100).yield_interest()
BankAccount.total_bank_account()
