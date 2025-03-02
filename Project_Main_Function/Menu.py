from Ultilities import slow_print

def menu_generator(options):
    """Yields a formatted menu option list."""
    for index, option in enumerate(options):
        yield f"{index + 1}. {option}"

def display_menu(options):
    """Displays the menu options."""
    slow_print("\n=== Game Menu ===", delay=0.05)
    for item in menu_generator(options):
        slow_print(item, delay=0.05)

def handle_choice(options):
    """Handles user input for menu selection."""
    while True:
        try:
            choice = int(input("\nSelect an option: ").strip())
            if 1 <= choice <= len(options):
                slow_print(f"You chose: {options[choice - 1]}", delay=0.05)
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
        slow_print("Starting game...", delay=0.07)
    elif selected_option == 2:
        slow_print("Loading game...", delay=0.07)
    elif selected_option == 3:
        slow_print("Exiting game...", delay=0.07)
    else:
        slow_print("Unexpected error.", delay=0.07)

if __name__ == "__main__":
    main()
