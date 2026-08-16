class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def show(self):
        print(f"Name of the animal is {self.name} and its species is {self.species}")
        
class Cat(Animal):
    def __init__(self, name,breed):
        Animal.__init__(self,name, species="Cat")
        self.breed=breed
    def show(self):
        Animal.show(self)
        print(f"breed of the animal is {self.breed}")    
        
class Persian(Cat):
    def __init__(self, name, color):
        Cat.__init__(self,name, breed="Persian")
        self.color=color
    def show(self):
        Cat.show(self)
        print(f"color of the animal is {self.color}")

a=Persian("lulli","white")
a.show()