    #Hybrid Inheritance

class Animal:
    def __init__(self,species):
        self.species=species
    def show(self):
        print(f'Speicies of the animal is {self.species}')

class Lion(Animal):
    def __init__(self,species):
        Animal.__init__(self,species)
        self.nature='Lions are highly social, deeply affectionate family cats that balance hours\n of lazy relaxation with fierce, collaborative hunting and territory defense.' 
    def show(self):
        Animal.show(self)
        print(f'the nature of {self.species} is {self.nature}')

class Tiger(Animal):
    def __init__(self,species):
        Animal.__init__(self,species)
        self.nature='Tigers are solitary, highly territorial\n, and fiercely independent stealth hunters that rely on camouflage, patience\n, and pure individual strength to survive.' 
    def show(self):
        Animal.show(self)
        print(f'the nature of {self.species} is {self.nature}')  

class Predator_Habitat(Lion,Tiger):
    def __init__(self, species):
        if species=="Lion":
            Lion.__init__(self,species)
        elif species=="Tiger":
            Tiger.__init__(self,species)
           
    def show(self):
        if self.species=="Lion":
            Lion.show(self) 
        elif self.species=="Tiger":
            Tiger.show(self)  

a=Predator_Habitat("Tiger")
a.show()


    #Hierarchical Inheritance
class Animals:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f'Name of the animal is {self.name}')

class Dog(Animals):
    def __init__(self, name):
        super().__init__(name)
        self.sound="Barks"
    def show(self):
        print(f'{self.name} is a \"Dog\" and he/she {self.sound}')

class Cat(Animals):
    def __init__(self, name):
        super().__init__(name)
        self.sound="Meows"
    def show(self):
            print(f'{self.name} is a \"Dog\" and he/she {self.sound}')

a=Dog("lulli")
a.show()