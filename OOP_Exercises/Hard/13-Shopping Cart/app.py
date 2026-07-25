import os
from user import *
from store import *
from products import *
from cart import *


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class App:
    def __init__(self):
        self.running = True
        
    def run(self):
        self.__welcome()
        while self.running:
            self.__menu()
            choice = input(f"\n --> ").strip()
            self.__choice(choice)
            
    def __welcome(self):
        print("="*30)
        print("Welcome to Codex Gigas")
        print("="*30)
        
    def __menu(self):
        print(f"\n1. For admin\n2. For customer")
        
    def __choice(self,choice):
        self.rotation = True
        if choice == '1':
            name = input("Enter user name: ")
            email = input("Enter user E-mail: ")
            person = Admin(name,email)
            passkey = input("Enter the admin password: ")
             
            if passkey == person.password:
                print("Logged in as Admin")
                print('\n1.Add Product\n2.Edit Product\n.Search Product\n4View All Products\n5.Delete Product')
                admin_choice = input("\n -->")
                if admin_choice == '1':
                    Admin.add_product()
                if admin_choice == '4':
                    Admin.view_product()
                    
                
                
                
        
        if choice == '2':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            password = input("Enter password: ")
            
            person = Customer(name,email,password)
            print("Logged in as Customer")
            print("\n1.View store\n2.View cart")
            
            
            
            
            

if __name__ == "__main__":
    app = App()
    app.run()