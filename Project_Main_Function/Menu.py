def menu_generator(options):
    for index, option in enumerate(options):
        yield f"{index + 1}. {option}"

def display_menu(options):
    print("Menu")
    for item in menu_generator(options):
        print(item)

if __name__ == "__main__":
    menu_option = ["Start Game", "Load Game", "Exit Game"]
    display_menu(menu_option)