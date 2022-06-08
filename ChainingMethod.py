from BankAccount import account

class User:	
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = account(int_rate=2,balance=0)

    def make_deposit(self, amount):	
        self.account_balance.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(self.name, self.account_balance.display_account_info())
        return self

Hala = User("Hala", "Hala@python.com")
Tala = User("Tala", "Tala@python.com")
Joudi = User("Joudi","Joudi@python.com")
#----------------------------

Hala.make_deposit(5000).make_deposit(1500).make_deposit(400).make_withdrawal(100).display_user_balance()

#----------------------------

Tala.make_deposit(6000).make_deposit(500).make_withdrawal(250).make_withdrawal(200).display_user_balance()

#----------------------------

Joudi.make_deposit(4000).make_withdrawal(500).make_withdrawal(250).make_withdrawal(250).display_user_balance()

#----------------------------