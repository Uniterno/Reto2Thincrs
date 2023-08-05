import datetime

import peewee

from db.migrations import create_db
from controllers.user_controller import UserController
from controllers.account_controller import AccountController
from controllers.card_controller import CardController
from controllers.charge_controller import ChargeController
from controllers.payment_controller import PaymentController


# CRUD USER

def create_user():
    print("You are creating a new user, please fill in the required info...")
    name = input("Name: ")
    age = int(input("Age: "))
    try:
        user = UserController.create_user(age=age, name=name)
        print("User created correctly")
        account_limit = int(input("Account limit: "))
        AccountController.create_account(user=user,
                                         balance=0,
                                         open_date=datetime.datetime.now(),
                                         limit=account_limit)
    except ValueError:
        print("User could not be created!")


def read_user():
    name = input("Please input the user name to search: ")
    try:
        user = UserController.get_user_by_name(name=name)
        if user is not None:
            print("Successfully found user!")
            print("ID: ", user.id)
            print("Name: ", user.name)
            print("Age: ", user.age)
            account = AccountController.get_account_by_user(user=user)
            if account is not None:
                print("-- Associated account --")
                print("Balance: ", account.balance)
                print("Open date: ", account.open_date)
                print("Limit: ", account.limit)
                card = CardController.get_card_by_account(account=account)
                if card:
                    print("-- Associated card --")
                    print("Name: ", card.name)
                    print("CVV not shown for security reasons")
        else:
            print("Couldn't find an user with that name!")

    except ValueError:
        print("User could not be found!")


def update_user_name():
    name = input("Please input the user name to update: ")
    try:
        user = UserController.get_user_by_name(name=name)
        if user is not None:
            print("Successfully found user!")
            new_name = input(f"Current name: {user.name} | Please input new name: ")
            try:
                UserController.update_name(user=user, name=new_name)
            except ValueError:
                print("Couldn't update name!")
        else:
            print("Couldn't find an user with that name!")

    except ValueError:
        print("User could not be updated!")


def update_user_age():
    name = input("Please input the user name to update: ")
    try:
        user = UserController.get_user_by_name(name=name)
        if user is not None:
            print("Successfully found user!")
            new_age = int(input(f"Current age: {user.age} | Please input new age: "))
            try:
                UserController.update_age(user=user, age=new_age)
            except ValueError:
                print("Couldn't update age!")
        else:
            print("Couldn't find an user with that name!")

    except ValueError:
        print("User could not be updated!")


def delete_user():
    name = input("Please input the user name to delete: ")
    try:
        user = UserController.get_user_by_name(name=name)
        if user is not None:
            print("Successfully found user!")

            try:
                UserController.delete_user(user=user)
            except ValueError:
                print("Couldn't delete user!")
        else:
            print("Couldn't find an user with that name!")

    except ValueError:
        print("User could not be deleted!")


def menu_user():
    menu_functions = {
        1: create_user,
        2: read_user,
        3: update_user_name,
        4: update_user_age,
        5: delete_user
    }

    while True:
        print("\n===== MANAGE USER =====")
        print("1. Create new user")
        print("2. Search user")
        print("3. Update user's name")
        print("4. Update user's age")
        print("5. Delete user")
        print("6. Go back")
        print("================")
        choice = input("Enter your choice (1-6): ")

        try:
            choice = int(choice)
            if choice in menu_functions:
                menu_functions[choice]()
            elif choice == 6:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number (1-5).")


def add_card():
    pass


def update_card():
    pass


def delete_card():
    pass


def menu_cards():
    menu_functions = {
        1: add_card,
        2: update_card,
        3: delete_card
    }

    while True:
        print("\n===== MANAGE CARD =====")
        print("1. Create new card")
        print("2. Update card")
        print("3. Delete card ")
        print("4. Go back")
        print("================")
        choice = input("Enter your choice (1-4): ")

        try:
            choice = int(choice)
            if choice in menu_functions:
                menu_functions[choice]()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")


def manage_users():
    menu_user()


def manage_cards():
    menu_cards()


def make_charge():
    pass


def fund_account():
    print("You're about to make a payment, please input the user name to proceed.")
    name = input("Name: ")
    try:
        user = UserController.get_user_by_name(name=name)
        if user is not None:
            account = AccountController.get_account_by_user(user=user)
            if account is not None:
                print("-- Account found --")
                print("Balance: ", account.balance)
                print("Open date: ", account.open_date)
                print("Limit: ", account.limit)
                amount = float(input("Payment amount: "))
                if AccountController.update_balance(account=account, amount=amount):
                    try:
                        PaymentController.make_payment(account=account, date_time=datetime.datetime.now(), amount=amount)
                        print("Payment successful!")
                    except peewee.IntegrityError:
                        print("This account has no associated cards")
                else:
                    print("An error has occurred processing your payment. Please verify your balance and limit")
        else:
            print("This user doesn't exist, please verify the name is correct")

    except RuntimeError:
        print("An unexpected error has occurred!")


def update_account_limit():
    print("You're about to change the limit of an account.")
    name = input("Name of the owner of the account: ")
    try:
        user = UserController.get_user_by_name(name=name)
        if user is not None:
            account = AccountController.get_account_by_user(user=user)
            if account is not None:
                print("-- Account found --")
                print("Balance: ", account.balance)
                print("Open date: ", account.open_date)
                print("Limit: ", account.limit)
                new_limit = float(input("New limit: "))
                if account.balance > new_limit:
                    print("The current balance of the account must not exceed the new limit! Operation aborted...")
                elif AccountController.update_limit(account=account, limit=new_limit):
                    print("Limit updated successfully!")
                else:
                    print("An error has occurred processing your request.")
        else:
            print("This user doesn't exist, please verify the name is correct")

    except RuntimeError:
        print("An unexpected error has occurred!")


def quit_program():
    print("Exiting the program.")
    exit()


def show_menu():
    print("\n===== MENU =====")
    print("1. Manage Users")
    print("2. Manage Cards")
    print("3. Make Charge")
    print("4. Make Payment")
    print("5. Update Account limit")
    print("6. Quit system")
    print("================")


def main():
    menu_functions = {
        1: manage_users,
        2: manage_cards,
        3: make_charge,
        4: fund_account,
        5: update_account_limit,
        6: quit_program
    }

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        try:
            choice = int(choice)
            if choice in menu_functions:
                menu_functions[choice]()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number (1-6).")


if __name__ == "__main__":
    create_db('./db/db_oltp.db')
    main()
