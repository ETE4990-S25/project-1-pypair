import sys
import os 
import json
import logging
import time
import textwrap
from Player import Mage, Warrior, Shadow, Archer
from Inventory import display_inventory, Item



# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Construct the relative path to the JSON file
items_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Project_Json", "Items.json")
save_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Project_Json", "save_data.json")

def slow_print(text, delay=0.05):
    """Prints text one character at a time with a delay for a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to a new line after printing the text


def clear_screen():
    """Clears the terminal screen for better visibility."""
    os.system("cls" if os.name == "nt" else "clear")

def wrap_text(text, width=80):
    """Wraps text to a specified width for better display."""
    return "\n".join(textwrap.wrap(text, width))

def save_game(player):
    """Saves the player's game to a JSON file."""
    player_data = {
        "name": player.name,
        "player_class": player.__class__.__name__,
        "level": player.level,
        "hp": player.hp,
        "mana": player.mana,
        "stamina": player.stamina,
        "strength": player.strength,
        "dexterity": player.dexterity,
        "intelligence": player.intelligence,
        "experience": player.experience,
        "inventory": [item.name for item in player.inventory]
    }
    with open(save_path, "w") as file:
        json.dump(player_data, file, indent=4)
    logging.info("Game saved successfully.")


def load_game():
    """Loads the player's game from a JSON file and returns a Player object."""
    try:
        with open(save_path, "r") as file:
            data = json.load(file)

        player_class = {"Mage": Mage, "Warrior": Warrior, "Shadow": Shadow, "Archer": Archer}
        if "class" not in data or data["class"] not in player_class:
            logging.error("Invalid or missing class in save data. Starting a new game.")
            return None


        player = player_class[data["class"]](data["name"])
        
        # Restore attributes
        player.level = data["level"]
        player.hp = data["hp"]
        player.mana = data["mana"]
        player.stamina = data["stamina"]
        player.strength = data["strength"]
        player.dexterity = data["dexterity"]
        player.intelligence = data["intelligence"]
        player.experience = data["experience"]
        player.inventory = [Item(name=item_name, item_type="unknown", rarity="unknown") for item_name in data["inventory"]]

        logging.info("Game loaded successfully.")
        return player
    except (FileNotFoundError, json.JSONDecodeError):
        logging.warning("No valid saved game found.")
        return None
