import json
import logging
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

    
    # Determine demon tier based on node progression
    node_list = list(storyline.keys())
    node_index = node_list.index(node)
    total_nodes = len(node_list)
    tier = 1

    # Tier ranges based on node index
    if node_index >= 10:  # Tier 3 starts at index 10
        tier = 3
    elif node_index >= 7:  # Tier 2 starts at index 7
        tier = 2 
    elif node_index >= 4:  # Tier 1 starts at index 4
        tier = 1

    # Handle event (combat or item)
    if "event" in event:
        if event["event"] == "combat":
            demon = spawn_demon(f"tier_{tier}")
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

    def handle_inventory():
        display_inventory(player.inventory)

    def handle_exit():
        slow_print("Exiting game...", delay=0.02)
        return True  # Signal to exit the loop

    def handle_use_item():
        item_name = input("Enter the item name to use: ").strip()
        use_item(player, item_name)

    def handle_start():
        if "menu_link" in storyline:
            progress_story(player, "menu_link", storyline)
        else:
            logging.error("Storyline not found.")
        return True  # Signal to exit the loop

    def handle_invalid():
        slow_print("Invalid choice. Try again.", delay=0.02)

    # Map user choices to corresponding functions
    actions = {
        "inventory": handle_inventory,
        "exit": handle_exit,
        "use item": handle_use_item,
        "start": handle_start,
    }

    while True:  # Allow interaction before starting
        slow_print("\nYou are in town. What would you like to do?", delay=0.02)
        slow_print("[start] Begin your adventure", delay=0.02)
        slow_print("[inventory] Check Inventory", delay=0.02)
        slow_print("[use item] Use an Item", delay=0.02)
        slow_print("[exit] Exit the game", delay=0.02)

        choice = input("Choose an action: ").strip().lower()
        action = actions.get(choice, handle_invalid)
        if action() is True:  # Exit the loop if the action signals to do so
            break
