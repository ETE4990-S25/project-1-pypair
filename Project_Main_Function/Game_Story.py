import json
import os
import textwrap
from Ultilities import slow_print, clear_screen, wrap_text
from Combat_System import combat, spawn_demon
from Player import Mage, Warrior, Shadow, Archer
from Inventory import display_inventory, use_item

# Load storyline JSON
def load_story():
    storyline_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Project_Json", "Storyline.json")
    try:
        with open(storyline_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: Storyline file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in storyline.")
        return {}

# Storyline progression
def progress_story(player, node, storyline):
    if node not in storyline:
        slow_print("Invalid story path.", delay=0.02)
        return
    
    event = storyline[node]

    # Display story text
    clear_screen()
    slow_print(wrap_text(event["text"]), delay=0.02)

    # Handle event (combat or item)
    if "event" in event:
        if event["event"] == "combat":
            demon = spawn_demon("tier_1")
            if demon:
                combat(player, demon, node)
            else:
                slow_print("No demons available to fight!", delay=0.02)
        elif event["event"] == "item":
            item = event["item"]
            slow_print(f"You obtained {item}!", delay=0.02)
            player.inventory.append(item)

    while True:
        slow_print("\nWhat do you do?")
        for key, value in event.get("choices", {}).items():
            slow_print(f"[{key}] {value}", delay=0.02)

        # Always allow inventory check and item usage
        slow_print("[inventory] Check Inventory", delay=0.02)
        slow_print("[use item] Use an Item", delay=0.02)
        
        choice = input("Choose an action: ").strip().lower()

        if choice == "inventory":
            display_inventory(player.inventory)
            continue  # Loop back to show options again
        elif choice == "use item":
            use_item(player)
            continue  # Allow using multiple items before choosing an action
        elif choice in event.get("choices", {}):
            next_node = event["choices"][choice]
            progress_story(player, next_node, storyline)  # Move forward
            return  # Stop asking for input

        slow_print("Invalid choice. Please try again.", delay=0.02)
                



def start_story(player):
    """Starts the storyline with the provided player instance."""
    storyline = load_story()
    
    while True:  # Allow interaction before starting
        slow_print("\nYou are in town. What would you like to do?")
        slow_print("[start] Begin your adventure")
        slow_print("[inventory] Check Inventory")
        slow_print("[use item] Use an Item")
        
        choice = input("Choose an action: ").strip().lower()

        if choice == "inventory":
            display_inventory(player.inventory)
        elif choice == "use item":
            item_name = input("Enter the item name to use: ").strip()
            use_item(player, item_name)
        elif choice == "start":
            if "menu_link" in storyline:
                progress_story(player, "menu_link", storyline)
            else:
                slow_print("Error: Missing 'menu_link' in storyline data.", delay=0.02)
            return
        else:
            slow_print("Invalid choice. Try again.")
