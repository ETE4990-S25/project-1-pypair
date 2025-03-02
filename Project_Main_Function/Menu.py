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
    clear_screen()
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
                return choice
            else:
                slow_print("Invalid choice. Please select a valid option.", delay=0.05)
        except ValueError:
            slow_print("Invalid input. Please enter a number.", delay=0.05)

def start_storyline():
    """Displays the game's introduction storyline with slow printing."""
    clear_screen()
    slow_print("\nThe world has fallen into darkness...", delay=0.07)
    slow_print("Demonic creatures roam the land, terrorizing villages and devouring the innocent.", delay=0.07)
    slow_print("Only a handful of warriors dare to stand against the abyss...", delay=0.07)
    
    input("\nPress Enter to continue...")  # Pause for player interaction
    clear_screen()
    
    slow_print("You are one of them.", delay=0.07)
    slow_print("A lone hero, standing at the edge of fate.", delay=0.07)
    slow_print("Your journey begins now...", delay=0.07)

    input("\nPress Enter to enter the world...")  # Final pause before gameplay

def execute_option(choice):
    """Executes the selected menu option."""
    if choice == 1:
        start_storyline()
        gamestart() #Placeholder for the game start function
    elif choice == 2:
        slow_print("Loading game...", delay=0.07)
    elif choice == 3:
        slow_print("Exiting game...", delay=0.07)
    else:
        slow_print("Unexpected error.", delay=0.07)

def main():
    menu_options = ["Start Game", "Load Game", "Exit Game"]
    display_menu(menu_options)
    selected_option = handle_choice(menu_options)
    execute_option(selected_option)

if __name__ == "__main__":
    main()
