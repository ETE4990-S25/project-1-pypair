import json

def display_inventory(inventory):
    print("Player Inventory:")
    print("=" * 30)
    for item in inventory:
        print(f"Name: {item['name']}")
        print(f"Type: {item['type']}")
        print(f"Rarity: {item['rarity']}")
        if 'damage' in item:
            print(f"Damage: {item['damage']}")
        if 'defense' in item:
            print(f"Defense: {item['defense']}")
        if 'effect' in item:
            print(f"Effect: {item['effect']}")
        print(f"Requirement: {item['requirement']}")
        print(f"Description: {item['description']}")
        print("-" * 30)

placeholder = [
    {
        "name": "Wooden Sword",
        "type": "sword",
        "rarity": "common",
        "damage": 6,
        "requirement": {"strength": 5},
        "description": "A simple but sturdy wooden sword."
    },
    {
        "name": "Leather Armor",
        "type": "armor",
        "rarity": "common",
        "defense": 10,
        "requirement": {"strength": 4},
        "description": "Basic leather armor offering minimal protection."
    }
]

display_inventory(placeholder)