class details:
    college="COEP"

    def __init__(self,name):
        self.name=name
    @classmethod
    def clgname(cls,clg):
        cls.college=clg
    def show(self):
        print(f"My name is {self.name} I am student of {self.college}")


a=details("Rajveer")

  
a.clgname("iit")
a.show()  
print(details.college)  #class variable remains same

