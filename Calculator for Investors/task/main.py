def main():
    MAIN_MENU = {
        '0': "Exit",
        '1': "CRUD operations",
        '2': "Show top ten companies by criteria"
    }

    CRUD_MENU = {
        '0': "Back",
        '1': "Create a company",
        '2': "Read a company",
        '3': "Update a company",
        '4': "Delete a company",
        '5': "List all companies"
    }

    TOP_TEN_MENU = {
        '0': "Back",
        '1': "List by ND/EBITDA",
        '2': "List by ROE",
        '3': "List by ROA"
    }

    while True:
        print("MAIN MENU")
        for item in MAIN_MENU:
            print(f"{item} {MAIN_MENU[item]}")

        option = input("\nEnter an option:\n")
        if option == '0':
            print("Have a nice day!")
            break
        elif option == '1':
            print("\nCRUD MENU")
            display_menu(CRUD_MENU)
        elif option == '2':
            print("\nTOP TEN MENU")
            display_menu(TOP_TEN_MENU)
        else:
            print("Invalid option!\n")


def display_menu(menu: dict[str, str]):
    for item in menu:
        print(f"{item} {menu[item]}")
    print()

    choices = list(menu.keys())
    choice = input("Enter an option: ")
    if choice == '0':
        return
    elif choice in choices:
        print("\nNot implemented!")


if __name__ == '__main__':
    main()
