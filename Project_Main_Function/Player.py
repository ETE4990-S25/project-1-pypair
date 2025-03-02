## Imports
import os
import json
import logging
from Inventory import display_inventory

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Construct the relative path to the JSON file
json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Project_Json", "Items.json")

# Load JSON data
try:
    with open(json_path, "r") as file:
        items_data = json.load(file)
except FileNotFoundError:
    logging.error(f"Error: Could not find {json_path}")
except json.JSONDecodeError:
    logging.error("Error: Invalid JSON format in Items.json")

## Function for player class
class Player:
### Player attributes
    def __init__(self, name: str, hp: int, mana: int, stamina: int, strength: int, dexterity: int, intelligence: int):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.stamina = stamina
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.level = 1
        self.experience = 0
        self.exp_to_level = 10  # Base experience required for level 2
        self.inventory = []
        self.equipped_weapon = None
    
    def equip_weapon(self, weapon):
        if self.can_equip(weapon):
            self.equipped_weapon = weapon
            return f"{self.name} equipped {weapon['name']}!"
        return f"{self.name} cannot equip {weapon['name']}!"
    
    def can_equip(self, weapon):
        return False  # Default to not equipping anything
    
    def gain_experience(self, amount):
        self.experience += amount
        while self.experience >= self.exp_to_level:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.experience -= self.exp_to_level
        self.exp_to_level = int(self.exp_to_level * 1.5)

class Mage(Player):
    def level_up(self):
        super().level_up()
        self.hp += 5
        self.mana += 15
        self.stamina += 5
        self.intelligence += 5

class Warrior(Player):
    def level_up(self):
        super().level_up()
        self.hp += 15
        self.mana += 2
        self.stamina += 10
        self.strength += 5

class Shadow(Player):  # Thief class
    def level_up(self):
        super().level_up()
        self.hp += 7
        self.mana += 7
        self.stamina += 7
        self.strength += 2
        self.dexterity += 2
        self.intelligence += 2

class Archer(Player):
    def level_up(self):
        super().level_up()
        self.hp += 10
        self.mana += 5
        self.stamina += 15
        self.dexterity += 3
