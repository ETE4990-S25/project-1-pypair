import sys
import os 
import json
import logging
import time
import textwrap

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
    data = {
        "name": player.name,
        "level": player.level,
        "hp": player.hp,
        "mana": player.mana,
        "stamina": player.stamina,
        "strength": player.strength,
        "dexterity": player.dexterity,
        "intelligence": player.intelligence,
        "experience": player.experience,
        "inventory": [item.name for item in player.inventory.items]  # Saves item names only
    }
    with open(save_path, "w") as file:
        json.dump(data, file, indent=4)
    logging.info("Game saved successfully.")


def load_game(player):
    """Loads the player's game from a JSON file."""
    try:
        with open(save_path, "r") as file:
            data = json.load(file)
        # Restore player attributes
        player.name = data["name"]
        player.level = data["level"]
        player.hp = data["hp"]
        player.mana = data["mana"]
        player.stamina = data["stamina"]
        player.strength = data["strength"]
        player.dexterity = data["dexterity"]
        player.intelligence = data["intelligence"]
        player.experience = data["experience"]
        # Restore inventory with item names (attributes unknown at load time)
        player.inventory.items = [Item(name=item_name, item_type="unknown", rarity="unknown") for item_name in data["inventory"]]
        
        logging.info("Game loaded successfully.")
    except FileNotFoundError:
        logging.warning("No saved game found.")
    except json.JSONDecodeError:
        logging.error("Error loading saved game data.")