def menu_generator(options):
    """Yields a formatted menu option list."""
    for index, option in enumerate(options):
        yield f"{index + 1}. {option}"

def display_menu(options):
    """Displays the menu options."""
    print("\n=== Game Menu ===")
    for item in menu_generator(options):
        print(item)

def handle_choice(options):
    """Handles user input for menu selection."""
    while True:
        try:
            choice = int(input("\nSelect an option: ").strip())
            if 1 <= choice <= len(options):
                print(f"You chose: {options[choice - 1]}")
                return choice  # Returning choice for further processing
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    menu_options = ["Start Game", "Load Game", "Exit Game"]
    display_menu(menu_options)
    selected_option = handle_choice(menu_options)

    if selected_option == 1:
        print("Starting game...")
    elif selected_option == 2:
        print("Loading game...")
    elif selected_option == 3:
        print("Exiting game...")
    else:
        print("Unexpected error.")

if __name__ == "__main__":
    main()
