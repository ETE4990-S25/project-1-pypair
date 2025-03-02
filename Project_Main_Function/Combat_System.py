import os
import json
import random
import logging
from Player import Player, Mage, Warrior, Shadow, Archer

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Construct the relative path to the JSON file
demons_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Project_Json", "Demons.json")
items_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Project_Json", "Items.json")

# Load items from Items.json
try:
    with open(items_path, "r") as file:
        items_data = json.load(file)
except FileNotFoundError:
    logging.error(f"Error: Could not find {items_path}")
    items_data = {}
except json.JSONDecodeError:
    logging.error("Error: Invalid JSON format in Items.json")
    items_data = {}

# Load demons from Demons.json
try:
    with open(demons_path, "r") as file:
        demons_data = json.load(file)["demons"]
except FileNotFoundError:
    logging.error(f"Error: Could not find {demons_path}")
    demons_data = {}
except json.JSONDecodeError:
    logging.error("Error: Invalid JSON format in Demons.json")
    demons_data = {}

## Function to spawn demons randomly from a tier
def spawn_demon(tier):
    if tier in demons_data:
        return random.choice(demons_data[tier])
    return None

## Combat System
def combat(player, demon):
    logging.info(f"{player.name} encounters {demon['name']}!")
    while player.hp >0 and demon["hp"] > 0:
        print(f"\n{player.name}: HP {player.hp} | {demon['name']}: HP {demon['hp']}")
        action = input("Choose an action: (1) Attack, (2) Use Item, (3) Run: ")
        # Player actions
        if action == "1":   # Attack
            damage = calculate_damage(player, demon)    # Calculate damage
            demon["hp"] -= damage   # Deal damage to demon
            print(f"{player.name} dealt {damage} damage to {demon['name']}!")   # Print damage dealt
        elif action == "2":
            print("Using an item is not implemented yet!")
        elif action == "3":  # Run
            print(f"{player.name} tries to run away from {demon['name']}!")
            if random.random() < 0.2:  # 20% chance of getting hit while running
                demon_damage = demon["damage"] - (player.strength // 2)
                demon_damage = max(1, demon_damage)  # Ensure at least 1 damage
                player.hp -= demon_damage
                print(f"{demon['name']} strikes {player.name} while running for {demon_damage} damage!")
            else:
                print(f"{player.name} successfully escapes!")
            return
        #Demon attacks back if alive
        if demon["hp"] > 0:
            demon_damage = demon["damage"] - (player.strength // 2)
            demon_damage = max(1, demon_damage) # Ensure at least 1 damage is dealt
            player.hp -= demon_damage
            print(f"{demon['name']} strikes {player.name} for {demon_damage} damage!")
    #Check battle outcome
    if player.hp > 0:
        print(f"{player.name} defeated {demon['name']}! Gained {demon['exp']} XP!")
        player.gain_experience(demon["exp"])
    else:
        print(f"{player.name} was defeated by {demon['name']}...")

# Function to get primary stat for damage calculations
def get_primary_stat(player):
    if isinstance(player, Mage):
        return player.intelligence
    elif isinstance(player, Warrior):
        return player.strength
    elif isinstance(player, Shadow):
        return (player.dexterity + player.strength + player.intelligence) // 3
    elif isinstance(player, Archer):
        return player.dexterity


# Function to calculate player attack damage
def calculate_damage(player, demon):
    base_damage = 5 + (get_primary_stat(player) // 2)
    weapon_damage = player.equipped_weapon["damage"] if player.equipped_weapon else 0
    
    if isinstance(player, Mage):
        return base_damage + weapon_damage + (player.magic_power // 4)
    elif isinstance(player, Warrior):
        return base_damage + weapon_damage + (player.strength // 3)
    elif isinstance(player, Shadow):
        return base_damage + weapon_damage + (player.dexterity // 3)
    elif isinstance(player, Archer):
        return base_damage + weapon_damage + (player.crit_chance // 2)
    return base_damage + weapon_damage