# make_withdrawal
class User:
    def __init__(self):
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

guido = User()
print(guido.make_deposit(1000).make_withdrawal(200).account_balance)




# display username and balance
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance +=amount
        return self
    def make_withdrawal(self,amount):
        self.account_balance -=amount
        return self
    def display_user_balance(self):
        print(f'User:{self.first_name} {self.last_name}: ${self.account_balance}')

guido = User('Guido','van Rossum')
mimi = User('Mimi', 'Kar')
manish = User('Manish', 'Punjabi')

guido.make_deposit(150).make_deposit(500).make_deposit(1000).make_withdrawal(400).display_user_balance()

mimi.make_deposit(5000).make_deposit(3000).make_withdrawal(100).make_withdrawal(500).display_user_balance()

manish.make_deposit(3000).make_withdrawal(300).make_withdrawal(500).make_withdrawal(1500).display_user_balance()




#Bonus: transfer_money method

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance +=amount
        return self
    def make_withdrawal(self,amount):
        self.account_balance -=amount
        return self
    def transfer_money(self,first_name, amount):
        self.make_withdrawal(amount)
        first_name.make_deposit(amount)
        return self
    def display_user_balance(self):
        print(f'User:{self.first_name} {self.last_name}: ${self.account_balance}')

guido = User('Guido','van Rossum')
manish = User('Manish', 'Punjabi')

guido.make_deposit(150).make_deposit(500).make_deposit(1000).make_withdrawal(400).transfer_money(manish, 11).display_user_balance()

manish.make_deposit(3000).make_withdrawal(300).display_user_balance()
