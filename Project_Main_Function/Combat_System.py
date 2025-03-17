import os
import json
import random
import logging
from Player import Player, Mage, Warrior, Shadow, Archer
from Inventory import use_item, display_inventory

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

# Function to determine loot drops
def get_loot_drop(location):
    """Determines item drop rarity based on location."""
    if location in ["black_marsh", "forgotten_tower", "tamoe_highland", "monastery_gate", "catacombs"]:
        loot_pool = items_data.get("items", {}).get("intermediate", [])
    else:
        loot_pool = items_data.get("items", {}).get("beginner", [])

    return random.choice(loot_pool) if loot_pool else None

# Combat System
def combat(player, demon, location):
    """Handles combat between the player and a demon."""
    logging.info(f"{player.name} encounters {demon['name']}!")
    
    demon_hp = demon["hp"]
    demon_damage = demon["damage"]
    demon_exp = demon["exp"]
    
    while player.hp > 0 and demon["hp"] > 0:
        print(f"\n{player.name}: HP {player.hp} | {demon['name']}: HP {demon['hp']}")
        action = input("Choose an action: (1) Attack, (2) Use Item, (3) Run: ").strip()

        # Player actions
        if action == "1":  # Attack
            damage = calculate_damage(player, demon)
            demon["hp"] -= damage
            print(f"{player.name} dealt {damage} damage to {demon['name']}!")
        elif action == "2":  # Use Item
            item_name = input("Enter the item name to use: ").strip()
            use_item(player, item_name)
        elif action == "3":  # Run
            print(f"{player.name} tries to run away!")
            if random.random() < 0.2:  # 20% chance of getting hit while escaping
                demon_damage = max(1, demon["damage"] - (player.armor // 2))
                player.hp -= demon_damage
                print(f"{demon['name']} strikes {player.name} while escaping for {demon_damage} damage!")
            else:
                print(f"{player.name} successfully escapes!")
            return

        # Enemy's turn
        if demon["hp"] > 0:
            player_defense = getattr(player, "armor", 0)
            demon_damage = max(1, demon["damage"] - (player_defense // 2))
            player.hp -= demon_damage
            print(f"{demon['name']} strikes {player.name} for {demon_damage} damage!")

    # Check battle outcome
    if player.hp > 0:
        print(f"{player.name} defeated {demon['name']}! Gained {demon['exp']} XP!")
        player.gain_experience(demon["exp"])

        # Determine if an item drops
        if random.random() < 0.5:  # 50% chance to drop an item
            loot = get_loot_drop(location)
            if loot:
                player.inventory.append(loot)
                print(f"{player.name} found a {loot['name']} ({loot['rarity']})!")

    else:
        print(f"{player.name} was defeated by {demon['name']}...")

# Function to get primary stat for damage calculations
def get_primary_stat(player):
    primary_stats = {
        Mage: lambda p: p.intelligence,
        Warrior: lambda p: p.strength,
        Shadow: lambda p: (p.dexterity + p.strength + p.intelligence) // 3,
        Archer: lambda p: p.dexterity
    }
    return primary_stats.get(type(player), lambda p: 0)(player)

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