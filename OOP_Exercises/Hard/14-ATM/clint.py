class Clint:
    def __init__(self,clint_id,pin,balance):
        self.clint_id = clint_id
        self.__pin = pin
        self.__balance = balance
    
    
    def verify_pin(self, pin):
        return pin == self.__pin
    
        
    def deposit(self,amount):
        self.__balance += amount
    
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("\n Not sufficient balance")
    
    def change_pin(self,new_pin):
        self.__pin = new_pin
    
    def check_balance(self):
        return self.__balance