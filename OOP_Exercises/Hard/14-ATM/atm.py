from clint import Clint

class ATM:
    def __init__(self,clint):
        self.user = clint
    
    
    def deposit(self):
        amount = int(input("Amount: "))
        if amount > 0:
            self.user.deposit(amount)
        else:
            print("Please enter a valid amount number")
    
    def withdraw(self):
        pin = input("PIN: ")
        if self.user.verify_pin(pin):
            amount = int(input("Amount: "))
            self.user.withdraw(amount)
        else:
            print("PIN doesn't match")
    
    def change_pin(self):
        old_pin = input("Old PIN: ")
        new_pin = input("New PIN: ")
        
        if self.user.verify_pin(old_pin):
            self.user.change_pin(new_pin)
        else:
            print("PIN doesn't match")
    
    def check_balance(self):
        pin = input("PIN: ")
        if self.user.verify_pin(pin):
            balance = self.user.check_balance()
            print(f"Yor account balance is {balance} Tk")
        else:
            print("PIN doesn't match")