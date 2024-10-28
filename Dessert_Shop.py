value = 0
x = 0
class dessert():
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
    def __str__(self):
        return f"{self.amount * self.value}"
class candy(dessert):
    value += 2
    x = 1
class cookie(dessert):
    value += 4
    x = 2
class sundae(dessert):
    value += 6
    x = 3
class icecream(dessert):
    value += 8
    x = 4
class sprinkles(icecream):
    value += 8.25
    x = 5

    
