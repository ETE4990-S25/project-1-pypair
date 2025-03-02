import os
from Ultilities import slow_print

def clear_screen():
    """Clears the terminal screen for better visibility."""
    os.system("cls" if os.name == "nt" else "clear")

def menu_generator(options):
    """Yields a formatted menu option list."""
    for index, option in enumerate(options):
        yield f"{index + 1}. {option}"

def display_menu(options):
    """Displays the menu options."""
    clear_screen()  # Clears screen before showing the menu
    slow_print("\n=== Game Menu ===", delay=0.05)
    slow_print("=" * 20, delay=0.05)
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
                slow_print("Invalid choice. Please select a valid option.", delay=0.05)
        except ValueError:
            slow_print("Invalid input. Please enter a number.", delay=0.05)

def execute_option(choice):
    """Executes the selected menu option."""
    messages = {
        1: "Starting game...",
        2: "Loading game...",
        3: "Exiting game..."
    }
    slow_print(messages.get(choice, "Unexpected error."), delay=0.07)

def main():
    menu_options = ["Start Game", "Load Game", "Exit Game"]
    display_menu(menu_options)
    selected_option = handle_choice(menu_options)
    execute_option(selected_option)

if __name__ == "__main__":
    main()
