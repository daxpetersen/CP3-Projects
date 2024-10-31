import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.base_strength = 10
        self.base_defense = 5
        self.level = 1
        self.experience = 0
        self.experience_to_level = 100
        self.armor = 0
        self.shield = 0
        self.potions = 0
        self.weapon = None

    def get_strength(self):
        if self.weapon:
            return self.base_strength + self.weapon.strength
        return self.base_strength

    def get_defense(self):
        return self.base_defense + self.armor + self.shield

    def level_up(self):
        self.level += 1
        self.experience -= self.experience_to_level
        self.experience_to_level += 50
        self.health = round(self.health * 1.4)
        self.base_strength = round(self.base_strength * 1.4)
        self.base_defense = round(self.base_defense * 1.4)
        print(f"{self.name} leveled up! Now at Level {self.level} with increased stats!")

    def equip_armor(self, armor_value):
        self.armor += armor_value
        print(f"{self.name} equipped armor with defense value: {armor_value}")

    def equip_shield(self, shield_value):
        self.shield += shield_value
        print(f"{self.name} equipped a shield with defense value: {shield_value}")

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equipped a weapon: {weapon.name}")

    def restore_health(self):
        if self.potions < 5:
            self.health += 100
            self.potions -= 1
            print(f"{self.name}'s health has been restored to {self.health}!")
        else:
            print(f"{self.name} found an empty bottle...")

    def __str__(self):
        return (f"Level: {self.level} | Experience: {self.experience}/{self.experience_to_level}\n"
                f"Strength: {self.get_strength()} | Health: {self.health}\n"
                f"Defense: {self.get_defense()} | Speed: 5\n"
                f"Potions: {self.potions} | Weapon: {self.weapon.name if self.weapon else 'None'}")


class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = 20 + (level ** 4)
        self.strength = round(15 * (1.2 ** level)) 
        self.defense = round(10 * (1.15 ** level))  

    def get_damage(self, damage):
        damage *= (1.15 ** self.level)  
        return max(round(damage - self.defense), 1)

    def __str__(self):
        return (f"{self.name} (Level {self.level}): Health = {self.health}, "
                f"Strength = {self.strength}, Defense = {self.defense}")


class Armor:
    def __init__(self, defense_value):
        self.defense_value = defense_value


class Shield:
    def __init__(self, defense_value):
        self.defense_value = defense_value


class Weapon:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength


class Location:
    def __init__(self, name, monsters, weapons, armors, shields, keys, potions):
        self.name = name
        self.monsters = monsters
        self.weapons = weapons
        self.armors = armors
        self.shields = shields
        self.keys = keys
        self.potions = potions
        



collected_keys = []
def failed_flee(enemy):
        base_damage = enemy.get_damage(enemy.strength)
        damage = round(base_damage * random.uniform(0.8, 1.2))
        player.health -= damage*2
        print(f"{enemy.name} combos {player.name} for {damage} damage!")
def display_locations():
    print("\nYou can explore the following locations:")
    for location_name in locations.keys():
        print(f"- {location_name}")

location_order = ['Cave', 'Ruins', 'Desert', 'Mountain', 'Dungeon', 'Castle', 'Sky', 'Underworld']
current_location_index = 0

def explore(location_input):
    global current_location_index

    location = locations.get(location_input.title())
    if not location:
        print("Invalid location. Please try again.")
        return

    expected_location = location_order[current_location_index]
    if location_order.index(location_input.title()) > current_location_index:
        print(f"You can only explore locations up to {expected_location} at this stage.")
        return

    print(f"\nExploring the {location.name}...")

    

    def portal_to_final_boss():
        print(f"{player.name} has entered the portal to face the Final Boss!")
        monster_name = random.choice(location.monsters)
        monster_level = random.randint(max(1, player.level - 1), round(player.level * 1.6))
        boss_combat(monster_name, monster_level + 100)
        if enemy.health <= 0:
            print("YOU WON!")
            exit()

    while True:
        action_chance = random.randint(1, 20)
        if all(key in collected_keys for key in ['Cave Key', 'Ruins Key', 'Desert Key', 'Mountain Key', 'Dungeon Key', 'Castle Key', 'Sky Key', 'Underworld Key']):
            print("\nAll keys have been found! A portal to the Final Boss has appeared.")
            portal_to_final_boss()
            return

        elif action_chance <= 9:
            monster_name = random.choice(location.monsters)
            monster_level = random.randint(max(1, player.level - 1), round(player.level * 1.6))
            print(f"\n{player.name} encountered a {monster_name} (Level {monster_level})!")
            start_combat(monster_name, monster_level)
            
            if player.health <= 0:
                return

        elif action_chance <= 18:
            find_items(location)

        elif action_chance == 19:
            find_key(location)

        elif action_chance == 20:
            player.restore_health()

        continue_choice = input("\nDo you want to cobatntinue exploring this location? (yes/no): ").strip().lower()
        if continue_choice == 'no':
            current_location_index += 1
            if current_location_index >= len(location_order):
                print("All locations have been explored!")
                return
            print(f"You are now able to explore the next location: {location_order[current_location_index]}")
            return




def find_items(location):
    """Permanently increases the player's strength or defense when finding a new item."""
    item_chance = random.randint(1, 100)

    if item_chance <= 50:
        new_weapon = random.choice(location.weapons)
        player.base_strength = round(player.base_strength * 1.2)
        print(f"{player.name} found a {new_weapon.name}! New Strength is now {player.base_strength}.")

    elif item_chance <= 75:
        new_shield = random.choice(location.shields)
        player.base_defense = round(player.base_defense * 1.3)
        print(f"{player.name} found a shield! New Defense is now {player.base_defense}.")

    elif item_chance <= 100:
        new_armor = random.choice(location.armors)
        player.base_defense = round(player.base_defense * 1.2)
        print(f"{player.name} found armor! New Defense is now {player.base_defense}.")


key = 0
def find_key(location):
    """Checks if a key can be found in the location, adds it to collected_keys if not already there."""
    for key in location.keys:
        if key not in collected_keys:
            collected_keys.append(key)
            print(f"{player.name} found the {key}!")
            return
    print(f"{player.name} found a worthless key.")  

def find_potion(location):
    """Check if a potion can be found in the location."""
    if location.potions > 0:
        player.potions += 1
        location.potions -= 1
        print(f"{player.name} found a potion! Total potions: {player.potions}")

def start_combat(enemy_name, enemy_level):
    enemy = Enemy(enemy_name, enemy_level)
    print(f"\nA {enemy.name} (Level {enemy.level}) attacks!")
    
    while player.health > 0 and enemy.health > 0:
        print(f"\n{player.name}'s Health: {player.health}")
        print(f"{enemy.name}'s Health: {enemy.health}")

        action = get_action()
        
        if action == 'attack':
            attack(enemy)
        elif action == 'flee':
            if not flee_attempt(enemy.strength * 2):
                print(f"\n{player.name} successfully fled from the {enemy.name}!")
                return
            else:
                print(f"\n{player.name} failed to flee! The {enemy.name} lands a combo attack!")
                failed_flee(enemy)

        if enemy.health > 0:
            enemy_attack(enemy)

    
def boss_combat(enemy_name, enemy_level):
    enemy = Enemy(enemy_name, enemy_level)
    print(f"\nBoss {enemy.name} (Level {enemy.level}) attacks!")

    while player.health > 0 and enemy.health > 0:
        print(f"\n{player.name}'s Health: {player.health}")
        print(f"{enemy.name}'s Health: {enemy.health}")

        action = get_action() 
        
        if action == 'attack':
            attack(enemy)
        elif action == 'flee':
            if not flee_attempt(enemy.strength*2):
                print(f"\n{player.name} successfully fled from the {enemy.name}!")
                return
            else:
                print(f"\n{player.name} failed to flee! The {enemy.name} lands a combo attack!")
                failed_flee(enemy)
        if enemy.health > 0:
            enemy_attack(enemy)

    if player.health <= 0:
        print(f"\n{player.name} has been defeated by the {enemy.name}...")
        exit_game()
    else:
        print(f"\n{player.name} defeated the {enemy.name}!")
        gain_experience(enemy)

def get_action():
    while True:
        action = input("Choose an action: [attack, flee]: ").lower()
        if action in ['attack', 'a', 'flee', 'f']:
            return 'attack' if action in ['attack', 'a'] else 'flee'

def flee_attempt(enemy_strength):
    flee_chance = 5 / (5 + enemy_strength)
    return random.random() < flee_chance

def attack(enemy):
    base_damage = player.get_strength()
    damage = round(base_damage * random.uniform(0.8, 1.2))
    enemy.health -= damage
    print(f"{player.name} attacks {enemy.name} for {damage} damage!")

def enemy_attack(enemy):
    base_damage = enemy.get_damage(enemy.strength)
    damage = round(base_damage * random.uniform(1.0, 1.5)) 
    player.health -= damage
    print(f"{enemy.name} attacks {player.name} for {damage} damage!")


    
def gain_experience(enemy):
    exp_gain = enemy.level * 20
    player.experience += exp_gain
    print(f"{player.name} gained {exp_gain} experience!")

    if player.experience >= player.experience_to_level:
        player.level_up()


def exit_game():
    print("Game Over. Thanks for playing!")
    exit()


locations = {
    'Cave': Location('Cave', ['Skeleton'], [Weapon('Axe', 6)], [Armor(random.randint(15, 20))], [Shield(random.randint(15, 20))], ['Cave Key'], 1),
    'Ruins': Location('Ruins', ['Zombie'], [Weapon('Mace', 7)], [Armor(random.randint(20, 25))], [Shield(random.randint(20, 25))], ['Ruins Key'], 1),
    'Desert': Location('Desert', ['Scorpion'], [Weapon('Spear', 8)], [Armor(random.randint(25, 30))], [Shield(random.randint(25, 30))], ['Desert Key'], 1),
    'Mountain': Location('Mountain', ['Bear'], [Weapon('Club', 9)], [Armor(random.randint(30, 35))], [Shield(random.randint(30, 35))], ['Mountain Key'], 1),
    'Dungeon': Location('Dungeon', ['Giant'], [Weapon('Great Sword', 10)], [Armor(random.randint(35, 40))], [Shield(random.randint(35, 40))], ['Dungeon Key'], 1),
    'Castle': Location('Castle', ['Dragon'], [Weapon('Flame Sword', 12)], [Armor(random.randint(40, 45))], [Shield(random.randint(40, 45))], ['Castle Key'], 1),
    'Sky': Location('Sky', ['Harpy'], [Weapon('Lightning Bow', 11)], [Armor(random.randint(45, 50))], [Shield(random.randint(45, 50))], ['Sky Key'], 1),
    'Underworld': Location('Underworld', ['Demon'], [Weapon('Inferno Blade', 13)], [Armor(random.randint(50, 55))], [Shield(random.randint(50, 55))], ['Underworld Key'], 1),
}

if __name__ == "__main__":
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    while True:
        display_locations()
        location_input = input("Choose a location to explore: ")
        explore(location_input)

