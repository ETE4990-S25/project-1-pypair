import os
import json
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Construct the relative path to the JSON file
demons_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Project_Json", "Demons.json")


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