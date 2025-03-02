import Game_Story
import os
import textwrap
from Ultilities import slow_print, clear_screen, wrap_text

from Player import Mage, Warrior, Shadow, Archer



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

def choose_class():
    """Allows the player to choose a class before starting the game."""
    clear_screen()
    slow_print("Choose your class:", delay=0.05)
    classes = {
        "1": ("Mage", Mage),
        "2": ("Warrior", Warrior),
        "3": ("Shadow", Shadow),
        "4": ("Archer", Archer)
    }
    for key, (cls_name, cls) in classes.items():
        slow_print(f"{key}. {cls_name}", delay=0.05)
    
    while True:
        choice = input("Enter the number of your class: ").strip()
        if choice in classes:
            name = input("Enter your character's name: ").strip()
            return classes[choice][1](name)
        slow_print("Invalid choice. Please select a valid class.", delay=0.05)

def start_storyline():
    """Loads the storyline and starts the game."""
    player = choose_class()
    Game_Story.start_story(player)


def execute_option(choice):
    """Executes the selected menu option."""
    if choice == 1:
        start_storyline()
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
