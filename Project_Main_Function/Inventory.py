import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Item:
    def __init__(self, name, item_type, rarity):
        self.name = name
        self.item_type = item_type
        self.rarity = rarity

    def __repr__(self):
        return f"{self.rarity} {self.name} ({self.item_type})"


def display_inventory(inventory):
    """Displays the player's inventory."""
    print("\nPlayer Inventory:")
    print("=" * 30)
    if not inventory:
        print("Your inventory is empty.")
    for idx, item in enumerate(inventory, 1):
        print(f"{idx}. {item['name']} ({item['rarity']})")
        print(f"   Type: {item['type']}")
        if 'damage' in item:
            print(f"   Damage: {item['damage']}")
        if 'defense' in item:
            print(f"   Defense: {item['defense']}")
        if 'effect' in item:
            print(f"   Effect: {item['effect']}")
        print(f"   Requirement: {item['requirement']}")
        print(f"   {item['description']}")
        print("-" * 30)

def use_item(player):
    """Allows a player to use or equip an item via number selection."""
    if not player.inventory:
        logging.info("Your inventory is empty.")
        return
    
    print("\nSelect an item to use:")
    display_inventory(player.inventory)
    
    try:
        choice = int(input("Enter the item number to use (or 0 to cancel): "))
        if choice == 0:
            logging.info("Cancelled.")
            return
        
        if 1 <= choice <= len(player.inventory):
            item = player.inventory[choice - 1]
            
            # Check if it's a consumable item
            if "effect" in item:
                apply_item_effect(player, item)
                player.inventory.pop(choice - 1)  # Remove after use
                logging.info(f"{player.name} used {item['name']}!")
                return
            # Check if it's equippable (weapon or armor)
            elif "damage" in item or "defense" in item:
                if meets_requirements(player, item):
                    equip_item(player, item)
                    logging.info(f"{player.name} equipped {item['name']}!")
                else:
                    logging.warning(f"{player.name} does not meet the requirements to equip {item['name']}.")
                return
        else:
            logging.warning("Invalid selection. Try again.")
    except ValueError:
        logging.error("Invalid input. Please enter a number.")


def apply_item_effect(player, item):
    """Applies the effect of a consumable item."""
    if "effect" in item:
        effect = item["effect"]
        if "heals" in effect:
            heal_amount = int(effect.split()[1])  # Extract heal value from effect description
            max_hp = getattr(player, "max_hp", player.hp)  # Default max_hp to current hp if not defined
            player.hp = min(player.hp + heal_amount, max_hp)
            logging.info(f"{player.name} healed for {heal_amount} HP!")


def meets_requirements(player, item):
    """Checks if a player meets the requirements to equip an item."""
    for req, value in item["requirement"].items():
        if getattr(player, req, 0) < value:
            return False
    return True

def equip_item(player, item):
    """Equips a weapon or armor for the player."""
    if "damage" in item:
        player.equipped_weapon = item
        print(f"{player.name} equipped {item['name']} (Weapon).")
    elif "defense" in item:
        player.equipped_armor = item
        print(f"{player.name} equipped {item['name']} (Armor).")

def drop_item(player, item_name):
    """Allows a player to drop an item from their inventory."""
    for item in player.inventory:
        if item["name"].lower() == item_name.lower():
            player.inventory.remove(item)
            print(f"{player.name} dropped {item['name']}.")
            return
    print(f"{item_name} not found in inventory.")
