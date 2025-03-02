import json
import os
import textwrap
from Ultilities import slow_print
from Combat_System import combat, spawn_demon
from Player import Player
from Inventory import display_inventory

# Load storyline JSON
def load_storyline():
    storyline_path = os.path.join(os.path.dirname(__file__), "Project_Json", "Storyline.json")
    try:
        with open(storyline_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: Storyline file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in storyline.")
        return {}
    
# wrap text for better display
def wrap_text(text, width=80):
    return "\n".join(textwrap.wrap(text, width))

# Storyline progression
def progress_story(player, node, storyline):
    if node not in storyline:
        slow_print("Invalid story path.", delay=0.05)
        return
    
    event = storyline[node]
    slow_print(wrap_text(event["text"]), delay=0.05)
    
    if "event" in event:
        if event["event"] == "combat":
            demon = spawn_demon("tier_1")  # Adjust tier as needed
            combat(player, demon)
        elif event["event"] == "item":
            item = event["item"]
            slow_print(f"You obtained {item}!", delay=0.05)
            player.inventory.append(item)
        
    if "choices" in event:
        for key, value in event["choices"].items():
            slow_print(f"[{key}] {value}", delay=0.05)
        
        choice = input("Choose an action: ").strip().lower()
        if choice in event["choices"]:
            progress_story(player, event["choices"][choice], storyline)
        else:
            slow_print("Invalid choice. Try again.", delay=0.05)

if __name__ == "__main__":
    storyline = load_storyline()
    player = Player("Hero", 100, 50, 50, 10, 10, 10)  # Temporary player instance
    progress_story(player, "start", storyline)
