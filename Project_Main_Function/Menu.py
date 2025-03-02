def menu_generator(options):
    for index, option in enumerate(options):
        yield f"{index + 1}. {option}"

def display_menu(options):
    print("Menu")
    for item in menu_generator(options):
        print(item)

def handle_choice(options):
    while True:
        try:
            choice = int(input("Select an Option:"))
            if 1 <= choice <= len(options):
                print(f"You Chose {options[choice - 1]}")
                break
            else:
                print(f"Invalid Choice")
        except ValueError:
            print("Invalid Input")
    

if __name__ == "__main__":
    menu_option = ["Start Game", "Load Game", "Exit Game"]
    display_menu(menu_option)
    handle_choice(menu_option)