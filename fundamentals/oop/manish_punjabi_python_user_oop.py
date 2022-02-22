# make_withdrawal
class User:
    def __init__(self):
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount

guido = User()
guido.make_deposit(1000)
guido.make_withdrawal(200)
print(guido.account_balance)

# display username and balance
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance +=amount
    def make_withdrawal(self,amount):
        self.account_balance -=amount
    def display_user_balance(self):
        print(f'User:{self.first_name} {self.last_name}: ${self.account_balance}')

guido = User('Guido','van Rossum')
mimi = User('Mimi', 'Kar')
manish = User('Manish', 'Punjabi')

guido.make_deposit(150)
guido.make_deposit(500)
guido.make_deposit(1000)
guido.make_withdrawal(400)
guido.display_user_balance()

mimi.make_deposit(5000)
mimi.make_deposit(3000)
mimi.make_withdrawal(100)
mimi.make_withdrawal(500)
mimi.display_user_balance()

manish.make_deposit(3000)
manish.make_withdrawal(300)
manish.make_withdrawal(500)
manish.make_withdrawal(1500)
manish.display_user_balance()

#Bonus: transfer_money method

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance +=amount
    def make_withdrawal(self,amount):
        self.account_balance -=amount
    def transfer_money(self, amount, person):
        self.make_withdrawal(amount)
        person.make_deposit(amount)
    def display_user_balance(self):
        print(f'User:{self.first_name} {self.last_name}: ${self.account_balance}')

guido = User('Guido','van Rossum')
manish = User('Manish', 'Punjabi')

guido.make_deposit(150)
guido.make_deposit(500)
guido.make_deposit(1000)
guido.make_withdrawal(400)

manish.make_deposit(3000)
manish.make_withdrawal(300)

guido.transfer_money(11, manish)

guido.display_user_balance()
manish.display_user_balance()
