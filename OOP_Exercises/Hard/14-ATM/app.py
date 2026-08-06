import os
from clint import Clint
from atm import ATM


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    uid = input("ID: ")
    pin = input("PIN: ")
    balance = int(input("Balance: "))
    user = Clint(uid,pin,balance)
    atm = ATM(user)

    running = True

    while running:
        clear_screen()

        print("=" * 30)
        print("       ATM SYSTEM")
        print("=" * 30)
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Change PIN")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("\n--> ").strip()

        clear_screen()

        if choice == "1":
            atm.deposit()

        elif choice == "2":
            atm.withdraw()

        elif choice == "3":
            atm.change_pin()

        elif choice == "4":
            atm.check_balance()

        elif choice == "5":
            print("Thank you for using the ATM.")
            running = False

        else:
            print("Invalid choice.")

        if running:
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()