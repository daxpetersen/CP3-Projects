menu = ["Chicken","Mac and Cheese","White Pasta","Shrimp"]
class store:

    def __init__(self,name,pick,servings):
        self.name = name
        self.pick = pick
        self.servings = servings
    
    def calculate(self):
        if self.pick == "Shrimp":
            self.servings = self.servings * 3
            return "Shrimp", self.servings
            
        elif self.pick == "Chicken":
            self.servings = self.servings * 5
            return "Chicken", self.servings

        elif    self.pick == "Mac and Cheese":
            self.servings = self.servings * 7
            return "Mac and Cheese", self.servings

        elif    self.pick == "White Pasta":
            self.servings = self.servings * 9 
            return "White Pasta", self.servings
            
    def __str__(self):
        while self.name == "Shrimp":
            print("yes")
            break
        return (f"""
        Pick up {self.pick}
        For ${self.servings, self.name}
        """)
    @classmethod
    def stats(self):
        return store(input("What's your name? "), input("What would you like to eat? "), input("How many servings would you like? "))
        

for i in range(len(menu)):
    print(menu[i])
choice = store.stats()
print(choice.calculate())
