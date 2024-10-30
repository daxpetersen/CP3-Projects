# dessert.py

class DessertItem:
    def __init__(self, name: str):
        self.name = name

class Candy(DessertItem):
    def __init__(self, name: str, candy_weight: float, price_per_pound: float):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        return self.candy_weight * self.price_per_pound

class Cookie(DessertItem):
    def __init__(self, name: str, cookie_quantity: int, price_per_dozen: float):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def calculate_cost(self):
        return (self.cookie_quantity / 12) * self.price_per_dozen

class IceCream(DessertItem):
    def __init__(self, name: str, scoop_count: int, price_per_scoop: float):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def calculate_cost(self):
        return self.scoop_count * self.price_per_scoop

class Sundae(IceCream):
    def __init__(self, name: str, scoop_count: int, price_per_scoop: float, topping_name: str, topping_price: float):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price
# test_dessert.py
# testing part
from dessert import Candy, Cookie, IceCream, Sundae

def test_candy():
    candy_item = Candy("Chocolate", 2.5, 3.00)
    assert candy_item.calculate_cost() == 7.5
    assert candy_item.name == "Chocolate"
    assert candy_item.candy_weight == 2.5

def test_cookie():
    cookie_item = Cookie("Oatmeal Raisin", 24, 5.00)
    assert cookie_item.calculate_cost() == 10.0
    assert cookie_item.name == "Oatmeal Raisin"
    assert cookie_item.cookie_quantity == 24

def test_ice_cream():
    ice_cream_item = IceCream("Vanilla", 3, 2.50)
    assert ice_cream_item.calculate_cost() == 7.5
    assert ice_cream_item.name == "Vanilla"
    assert ice_cream_item.scoop_count == 3

def test_sundae():
    sundae_item = Sundae("Strawberry", 2, 2.50, "Whipped Cream", 1.00)
    assert sundae_item.calculate_cost() == 6.0  # 5.0 for ice cream + 1.0 for topping
    assert sundae_item.name == "Strawberry"
    assert sundae_item.topping_name == "Whipped Cream"
