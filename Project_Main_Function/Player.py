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
        self.level = 1
        self.experience = 0
        self.exp_to_level = 10  # Base experience required for level 2
    
    def equip_weapon(self, weapon):
        if self.can_equip(weapon):
            self.equipped_weapon = weapon
            return f"{self.name} equipped {weapon['name']}!"
        return f"{self.name} cannot equip {weapon['name']}!"
    
    def can_equip(self, weapon):
        return False  # Default to not equipping anything
    
    def gain_experience(self, amount):
        self.experience += amount
        while self.experience >= self.exp_to_level:
            self.level_up()
    
    def level_up(self):
        pass  # To be implemented in subclasses

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
    
    def can_equip(self, weapon):
        return weapon["type"] == "staff"
    
    def cast_spell(self):
        return f"{self.name} casts a powerful spell!"
    
    def level_up(self):
        self.level += 1
        self.experience -= self.exp_to_level
        self.exp_to_level = int(self.exp_to_level * 1.5)
        self.hp += 5
        self.mana += 15
        self.stamina += 5
        self.intelligence += 5
        return f"{self.name} has leveled up to Level {self.level}! Next level requires {self.exp_to_level} XP."

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
    
    def can_equip(self, weapon):
        return weapon["type"] == "sword"
    
    def attack(self):
        return f"{self.name} swings their mighty sword!"
    
    def level_up(self):
        self.level += 1
        self.experience -= self.exp_to_level
        self.exp_to_level = int(self.exp_to_level * 1.5)
        self.hp += 15
        self.mana += 2
        self.stamina += 10
        self.strength += 5
        return f"{self.name} has leveled up to Level {self.level}! Next level requires {self.exp_to_level} XP."
    
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
    
    def can_equip(self, weapon):
        return weapon["type"] == "dagger"
    
    def sneak_attack(self):
        return f"{self.name} performs a deadly sneak attack!"
    
    def level_up(self):
        self.level += 1
        self.experience -= self.exp_to_level
        self.exp_to_level = int(self.exp_to_level * 1.5)
        self.hp += 7
        self.mana += 7
        self.stamina += 7
        self.strength += 2
        self.dexterity += 2
        self.intelligence += 2
        return f"{self.name} has leveled up to Level {self.level}! Next level requires {self.exp_to_level} XP."
    
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
    
    def can_equip(self, weapon):
        return weapon["type"] == "bow"
    
    def shoot_arrow(self):
        return f"{self.name} fires a precise arrow!"
    
    def level_up(self):
        self.level += 1
        self.experience -= self.exp_to_level
        self.exp_to_level = int(self.exp_to_level * 1.5)
        self.hp += 10
        self.mana += 5
        self.stamina += 15
        self.dexterity += 3
        return f"{self.name} has leveled up to Level {self.level}! Next level requires {self.exp_to_level} XP."

# Example Usage
player = Warrior("Conan")
print(player.gain_experience(10))  # Should trigger level up
