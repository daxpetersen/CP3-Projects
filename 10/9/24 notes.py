class pokemon:
    def __init__(self, name, hp, typ, level):
        self.name = name
        self.hp = hp
        self.type = typ
        self.level = level
    def combat(self, other):
        if self.level > other.level:
            return self.name,"won!"
        elif self.level < other.level:
            return other.name, "won", self.name,"has been defeated!"
        else:
            return "it's a tie, both pokemon are to tired to continue, both are eliminated!"
    def __str__(self):
        return (f"""
            name: {self.name}
            type: {self.type}
            level: {self.level}
            HP: {self.hp}
""")
    
    
    def level_up(self):
        self.level +=1
        self.hp *= 1.321413
    @classmethod
    def pikachu(self):
        return pokemon(input("What's my name? "), 50, "Electric", 1)
    @classmethod
    def hp_update(poke):
        return poke.hp - 5


pika = pokemon.pikachu()
pika.hp = pokemon.hp_update(pika)
print(pika)