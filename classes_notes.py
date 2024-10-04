#We start with keyboard class and we name them using PacalCase
class Animal:
    #We start with the constructor
    def __init__(self, name, species, age, gender, rarity):
        self.name = name
        self.species = species
        self.gender = gender
        self.age = age
        self.rarity = rarity
    
#Makes a readable string
    def __str__(self):
        return f"""
        Name:{self.name}
        Age: {self.age}
        Species: {self.species}
        Gender: {self.gender}
        Rarity: {self.rarity}
        """
#Methods our function inside the class
    def fight(self, other):
        if len(self.name) > len(other.name):
            other.losses +=1
            return self.name
        elif len(self.name) < len(other.name):
            self.losses +=1
            return other.name
        else:
            self.losses +=1
            other.losses +=1
            return "Tie"
        

#We generally store objects in varibles!
cat = Animal("Tom", "cat", 21, "Male", "Common")
frog = Animal("Jarrod", "Poison Dart Frog", 502, "Female", "Rare")


#To call the object we call the object.name of the method(needed arguments)
print(cat.fight(frog))
cat.name = "Thomas"

cat.losses = 0
frog.losses = 0

print(cat.fight)