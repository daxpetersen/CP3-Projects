class PetStore:
    def __init__(self,name):
        self.name = name
        self.animals = []
    name = "Pet Smart"
    def add_pet(self, animal):
        #assert is like an if statement that says if animal is not in Animal than don't run the rest of this function
        assert isinstance(animal, Animal)
        self.animals.append(animal)
    
    def remove_pet(self, animal):
        try:
            self.animals.remove(animal)
        except:
            print("That animal doesnt exist")
        else:
            print(animal, "removed")

    def featured(self, name):
        for pet in self.animals:
            if pet.name == name:
                self.featured_pet = pet
                print("Featured pet . . .",pet)
                break
        else:
            print("There is no such pet")

    def get_featured(self):
        return self.featured_pet
    
    def feed(self):
        for pet in self.animals:
            pet.eat()

    def get_mammals(self):
        return self.get_by_type(Mammal)
    
    def get_reptiles(self):
        return self.get_by_type(Reptile)
    
    def get_by_type(self, typ):
        return [pet for pet in self.animals if isinstance(pet,typ)]
    

class Animal:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"""
        This is {self.name}
            """
    def eat(self):
        print(self.name, "eating", self.diet)

class Mammal(Animal):
    pass

class Cat(Mammal):
    diet = "mice"

class Dog(Mammal):
    diet = "kibble"


class Reptile(Animal):
    pass

class Snake(Reptile):
    diet = "rodents"

class Turtle(Reptile):
    diet = "carrots"


class Bird(Animal):
    pass

class Parrot(Bird):
    diet = "seeds"
store = PetStore(1)
store.add_pet(Turtle("Straw"))
store.add_pet(Turtle("Flash"))
store.add_pet(Cat("Joe"))
store.add_pet(Snake("Robin"))
store.featured("Flash")

