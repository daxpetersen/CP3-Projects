#composition is a class that exsists inside of another class



class Tech:
    def __init__(self,name,storage):
        self.name = name
        self.storage = int(storage)


    def __str__(self):
        return f"This is a {self.make} {self.model} from {self.year} "
    
    def __repr__(self):
        return f"Car {self.make}, {self.model} {self.year}, {self.engine}"
    #this method is for other programmers inorder to debug in order to tell them the class and alll attributes


class Phone(Tech):
    def __init__(self, color,name,storage):
        self.color = color
        super().__init__(name, storage)


    def __str__(self):
        return f"A {self.color} {self.name} with {self.storage} of storage."
    
    def __repr__(self):
        return f"Phone({self.name}, {self.storage}, {self.color})"
    

class Laptop(Tech):
    def __init__(self, size,name,storage):
        super().__init__(name, storage)
        self.size = int(size)

    def __str__(self):
        return f"{self.size}-inch {self.name} with {self.storage} of storage."
#to call a composite vclass you musee avess where it is saved within the class


















































