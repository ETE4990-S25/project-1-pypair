## Function for player class
class Player:
### Player attributes
    def __init__(self, name: str, hp: int, mana: int, stamina: int, strength: int, dexterity: int, intelligence: int):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.stamina = stamina
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

class Mage(Player):
    def __init__(self, name):
        self.name = name
        self.hp = 80
        self.mana = 150
        self.stamina = 60
        self.strength = 6
        self.dexterity = 10
        self.intelligence = 18
        self.magic_power = 25  # Unique attribute
    
    def cast_spell(self):
        return f"{self.name} casts a powerful spell!"
    
class Warrior(Player):
    def __init__(self, name):
        self.name = name
        self.hp = 150
        self.mana = 40
        self.stamina = 100
        self.strength = 18
        self.dexterity = 8
        self.intelligence = 6
        self.armor = 20  # Unique attribute
    
    def attack(self):
        return f"{self.name} swings their mighty sword!"
    
class Shadow(Player):  # Thief class
    def __init__(self, name):
        self.name = name
        self.hp = 90
        self.mana = 60
        self.stamina = 120
        self.strength = 8
        self.dexterity = 18
        self.intelligence = 10
        self.stealth = 30  # Unique attribute
    
    def sneak_attack(self):
        return f"{self.name} performs a deadly sneak attack!"
    
class Archer(Player):
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mana = 50
        self.stamina = 90
        self.strength = 10
        self.dexterity = 16
        self.intelligence = 8
        self.crit_chance = 5  # Unique attribute
    
    def shoot_arrow(self):
        return f"{self.name} fires a precise arrow!"