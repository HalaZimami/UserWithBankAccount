from msilib.schema import SelfReg
from tkinter import Y

class account:	
    def __init__(self,int_rate=1,balance=0):
        self.intRate=int_rate
        self.account_balance = balance
        self.intAmount = 0

    def deposit(self, amount):	
        self.account_balance += amount
        return self
    
    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    
    def display_account_info(self):
        self.yield_interest()
        print(f"Balance: {self.account_balance} interest rate: {self.intRate}% interest amount: {self.intAmount}")
        return self
    
    def yield_interest(self):
        if(self.account_balance != 0):
            self.intAmount=self.account_balance*(self.intRate/100)
            self.account_balance=self.account_balance-self.intAmount
        return self

Hala = account()
Tala = account()
