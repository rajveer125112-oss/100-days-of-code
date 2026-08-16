class Animals:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def makesound(self):
        print("Sound made by animal")

class Dog(Animals):
    def __init__(self, name, species):
        super().__init__(name, species)
    def intro(self):
        print(f"My pet name is {self.name} it is a {self.species}")    
    def sound(self):
        print(f"Sound made by {self.name} is \"Bark\" ")


class Cat(Animals):
    def __init__(self, name, species):
        super().__init__(name, species)
    def intro(self):
        print(f"My pet name is {self.name} it is a {self.species}")    
    def sound(self):
        print(f"Sound made by {self.name} is \"Meow\" ")
    def behaviour(self):
        print(f"{self.name} has a bad habit of scratching furniture, beaware!!!")



a=Cat("Momo","Persian")
a.intro() ,a.sound(),a.behaviour()
b=Dog("MAHORAGA","HUSKY")
b.intro()
b.sound()

