import json
import os
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

# Storyline progression
def progress_story(player, node, storyline):
    if node not in storyline:
        print("Invalid story path.")
        return
    
    event = storyline[node]
    print(f"\n{event['text']}")
    
    if "event" in event:
        if event["event"] == "combat":
            demon = spawn_demon("tier_1")  # Adjust tier as needed
            combat(player, demon)
        elif event["event"] == "item":
            item = event["item"]
            print(f"You obtained {item}!")
            player.inventory.append(item)
        
    if "choices" in event:
        for key, value in event["choices"].items():
            print(f"[{key}] {value}")
        
        choice = input("Choose an action: ")
        if choice in event["choices"]:
            progress_story(player, event["choices"][choice], storyline)

if __name__ == "__main__":
    storyline = load_storyline()
    player = Player("Hero", 100, 50, 50, 10, 10, 10)  # Temporary player instance
    progress_story(player, "start", storyline)
