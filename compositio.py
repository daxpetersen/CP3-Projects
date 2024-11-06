#composition is a class that exsists inside of another class



class Car:
    def __init__(self,make, model,year,engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def __str__(self):
        return f"This is a {self.make} {self.model} from {self.year} "
    
    def __repr__(self):
        return f"Car {self.make}, {self.model} {self.year}, {self.engine}"
    #this method is for other programmers inorder to debug in order to tell them the class and alll attributes


class Engine:
    def __init__(self, configuration,displacement,horsepower,torque):
        self.configuration = configuration
        self.displacement = displacement
        self.horsepower = horsepower
        self.toque = torque
    
    def ignite(self):
        print("vroom vroom")

    def __str__(self):
        return f"The engine is a {self.configuration} with {self.displacement}, {self.horsepower} horsepower and {self.toque} torque"
    def __repr__(self):
        return f"Car {self.configuration}, {self.displacement} {self.horsepower}, {self.toque}"
    
myEngine = Engine("V8",5.8,326,344)
myCar = Car("Nissan","Hyundai Elantre",2016,myEngine)

#to call a composite vclass you musee avess where it is saved within the class
print(myCar)
myCar.engine.ignite()

print(repr(myCar))

















































