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

def slow_print(text, delay = 0.05, enabled = True):
    """Prints text one character at a time with a delay for a typewriter effect."""
    if enabled:
        for char in text:
            print(char, end='', flush = True)
            time.sleep(delay)
        print()
    else:
        print(text)

def clear_screen():
    """Clears the terminal screen for better visibility."""
    os.system("cls" if os.name == "nt" else "clear")

def wrap_text(text, width=80):
    """Wraps text to a specified width for better display."""
    return "\n".join(textwrap.wrap(text, width))
