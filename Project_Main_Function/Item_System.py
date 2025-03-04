import os
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Construct the relative path to the JSON file
items_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Project_Json", "Items.json")

# Load items from Items.json
try:
    with open(items_path, "r") as file:
        items_data = json.load(file)["items"]
except FileNotFoundError:
    logging.error(f"Error: Could not find {items_path}")
    items_data = {}
except json.JSONDecodeError:
    logging.error("Error: Invalid JSON format in Items.json")
    items_data = {}

# Item class
class Item:
    def __init__(self, name, item_type, rarity, **attributes):
        self.name = name
        self.type = item_type
        self.rarity = rarity
        self.attributes = attributes
    
    def __str__(self):
        return f"{self.name} ({self.rarity}) - {self.type}: {self.attributes}"