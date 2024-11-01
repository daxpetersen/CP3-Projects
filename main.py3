import random

class Monster:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def attack(self):
        print(f"{self.name} from {self.origin} attacks in a mysterious way!")

    def summon(self):
        print(f"{self.name}, emerging from {self.origin}, appears with a chilling presence!")

class Vampire(Monster):
    def __init__(self, name, origin):
        super().__init__(name, origin)
        self.bloodlust_level = random.randint(5, 10)

    def attack(self):
        if self.bloodlust_level > 7:
            print(f"{self.name} sinks its fangs into a victim, draining them with insatiable hunger!")
        else:
            print(f"{self.name} gazes hypnotically, entrancing the victim before a swift bite!")
        self.bloodlust_level = max(1, self.bloodlust_level - 1)

    def replenish_bloodlust(self):
        self.bloodlust_level = 10
        print(f"{self.name} has replenished its bloodlust with a fresh victim!")

class Zombie(Monster):
    def __init__(self, name, origin):
        super().__init__(name, origin)
        self.hunger = random.choice(["Brains", "Flesh", "Souls"])

    def attack(self):
        print(f"{self.name} moans, 'Must have... {self.hunger}!' and lunges to devour the living!")
    
    def revive(self):
        print(f"{self.name} stirs again. You can’t keep a good zombie down...")

class Witch(Monster):
    def __init__(self, name, origin):
        super().__init__(name, origin)
        self.spells = ["Fireball", "Petrify", "Cursed Whispers", "Poisonous Mist"]

    def attack(self):
        spell = random.choice(self.spells)
        print(f"{self.name} casts {spell}, filling the air with dark magic!")
    
    def brew_potion(self):
        print(f"{self.name} brews a sinister potion... Beware!")

class Ghost(Monster):
    def __init__(self, name, origin):
        super().__init__(name, origin)
        self.is_visible = False

    def attack(self):
        visibility = "invisible" if not self.is_visible else "visible"
        print(f"{self.name} becomes {visibility} and lets out a wail that chills the soul!")
    
    def fade_in_out(self):
        self.is_visible = not self.is_visible
        state = "appears" if self.is_visible else "fades away"
        print(f"{self.name} {state}, flickering between this world and the next...")

dracula = Vampire("Count Dracula", "Transylvania")
dracula.summon()
dracula.attack()
dracula.replenish_bloodlust()
dracula.attack()

walker = Zombie("The Walking Dread", "A Forgotten Graveyard")
walker.summon()
walker.attack()
walker.revive()

morgana = Witch("Morgana", "Darkwood Forest")
morgana.summon()
morgana.attack()
morgana.brew_potion()

specter = Ghost("The Wailing Specter", "The Haunted Manor")
specter.summon()
specter.attack()
specter.fade_in_out()
specter.attack()
