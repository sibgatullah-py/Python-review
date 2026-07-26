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
        clear_screen()
        self.__welcome()
        while self.running:
            self.__menu()
            choice = input(f"\n --> ").strip()
            self.__choice(choice)

    def __welcome(self):
        print("=" * 30)
        print("Welcome to Codex Gigas")
        print("=" * 30)

    def __menu(self):
        print(f"\n1. For admin\n2. For customer")

    def __choice(self, choice):
        self.rotation = True

        if choice == '1':
            clear_screen()

            name = input("Enter user name: ")
            email = input("Enter user E-mail: ")
            person = Admin(name, email)
            passkey = input("Enter the admin password: ")

            while self.rotation:
                if passkey == person.password:
                    clear_screen()

                    print("Logged in as Admin")
                    print("\n1. Add Product")
                    print("2. Edit Product")
                    print("3. Search Product")
                    print("4. View All Products")
                    print("5. Delete Product")

                    admin_choice = input("\n --> ")

                    clear_screen()

                    if admin_choice == '1':  # done
                        Admin.add_product()
                        input("\nPress Enter to continue...")
                        clear_screen()

                    elif admin_choice == '2':
                        product_id = input("Product ID: ")
                        Admin.edit_product(product_id)
                        input("\nPress Enter to continue...")
                        clear_screen()

                    elif admin_choice == '3':
                        product_id = input("Product ID: ")
                        Admin.search_product(product_id)
                        input("\nPress Enter to continue...")
                        clear_screen()

                    elif admin_choice == '4':  # done
                        Admin.view_product()
                        input("\nPress Enter to continue...")
                        clear_screen()

                    elif admin_choice == '5':
                        product_id = input("Product ID: ")
                        Admin.delete_product(product_id)
                        input("\nPress Enter to continue...")
                        clear_screen()

                else:
                    print("Invalid password!")
                    input("\nPress Enter to continue...")
                    clear_screen()
                        
                
                
                
        
        if choice == '2':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            password = input("Enter password: ")
            person = Customer(name,email,password)
            
            while self.rotation:
                print("Logged in as Customer")
                print("\n1.View store\n2.View cart")
            
            
            
            
            

if __name__ == "__main__":
    app = App()
    app.run()