# For this assignment, we'll add some functionality to a class:

#     have a method decrease the user's balance by the amount specified
#     have a method print the user's name and account balance to the terminal
#     have a method decrease the user's balance by the amount and add that amount to other other_user's balance


class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)


monty = User('monty')
monty.make_deposit(100)
monty.make_deposit(300)
monty.make_deposit(50)
monty.make_withdrawal(150)
monty.display_user_balance()

python = User('python')
python.make_deposit(3000)
python.make_deposit(420)
python.make_withdrawal(1650)
python.make_withdrawal(725)
python.display_user_balance()

guido = User('guido')
guido.make_deposit(500)
guido.make_withdrawal(30)
guido.make_withdrawal(130)
guido.make_withdrawal(5)
guido.display_user_balance()

monty.transfer_money(guido, 100)
monty.display_user_balance()
guido.display_user_balance()
