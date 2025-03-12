from Game_Start import display_menu, handle_choice
from Player import Warrior, Mage, Shadow, Archer
from Combat_System import spawn_demon, combat

def start_game():
    name = input("Enter your character name: ")
    print("Choose your class:")
    classes = {"1": Warrior, "2": Mage, "3": Shadow, "4": Archer}
    print("1. Warrior\n2. Mage\n3. Shadow\n4. Archer")
    choice = input("Select class: ")

    if choice in classes:
        player = classes[choice](name)
        print(f"\nWelcome, {player.name} the {player.__class__.__name__}!")
    else:
        print("Invalid choice. Defaulting to Warrior.")
        player = Warrior(name)

    demon = spawn_demon("tier_1")
    if demon:
        combat(player, demon)
    else:
        print("No demons available to fight!")

if __name__ == "__main__":
    menu_options = ["Start Game", "Load Game", "Exit Game"]
    display_menu(menu_options)
    handle_choice(menu_options)
    start_game()
