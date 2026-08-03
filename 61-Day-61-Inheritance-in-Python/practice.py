class details:
    def __init__(self,name,position,city):
        self.name=name
        self.position=position
        self.city=city
    def info(self):
        print(f"My name is {self.name}, I am {self.position} , I live in city {self.city}")



class country(details):
    def __init__(self,name,position,city,country):
        details.__init__(self,name,position,city)           #calling parent class info
        self.country=country
    def info(self):
            print(f"My name is {self.name}, I am {self.position} , I live in city {self.city},I am from {self.country}")
    

a=details("Rajveer","Student","Pune")
a.info()

a=country("Rajveer","Student","Pune","India")
a.info()