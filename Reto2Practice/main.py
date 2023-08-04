from db.migrations import create_db


def option_one():
    print("You selected Option 1.")


def option_two():
    print("You selected Option 2.")


def option_three():
    print("You selected Option 3.")


def quit_program():
    print("Exiting the program.")
    exit()


def show_menu():
    print("\n===== MENU =====")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Quit")
    print("================")


def main():
    menu_functions = {
        1: option_one,
        2: option_two,
        3: option_three,
        4: quit_program
    }

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        try:
            choice = int(choice)
            if choice in menu_functions:
                menu_functions[choice]()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")


if __name__ == "__main__":
    create_db('./db/db_oltp.db')
    main()