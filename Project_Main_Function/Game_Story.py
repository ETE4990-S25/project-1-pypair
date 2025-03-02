import json
import os
import textwrap
from Ultilities import slow_print
from Combat_System import combat, spawn_demon
from Player import Mage, Warrior, Shadow, Archer
from Inventory import display_inventory
from Menu import clear_screen, wrap_text

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
        slow_print("Invalid story path.", delay=0.05)
        return
    
    event = storyline[node]
    clear_screen()
    slow_print(wrap_text(event["text"]), delay=0.05)
    
    if "event" in event:
        if event["event"] == "combat":
            demon = spawn_demon("tier_1")
            combat(player, demon)
        elif event["event"] == "item":
            item = event["item"]
            slow_print(f"You obtained {item}!", delay=0.05)
            player.inventory.append(item)
        
    if "choices" in event:
        while True:
            clear_screen()
            slow_print(wrap_text(event["text"]), delay=0.05)
            for key, value in event["choices"].items():
                slow_print(f"[{key}] {value}", delay=0.05)
            
            choice = input("Choose an action: ").strip().lower()
            if choice in event["choices"]:
                progress_story(player, event["choices"][choice], storyline)
                break
            else:
                slow_print("Invalid choice. Try again.", delay=0.05)

def start_story(player):
    """Starts the storyline with the provided player instance."""
    storyline = load_story()
    if "menu_link" in storyline:
        progress_story(player, "menu_link", storyline)
    else:
        slow_print("Error: Missing 'menu_link' in storyline data.", delay=0.05)
