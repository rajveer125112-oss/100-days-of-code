class details:
    def __init__(self,name,mis,city):
        self.name=name
        self.mis=mis
        self.city=city
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1],string.split("-")[2])
    def show(self):
        print(f"My name is {self.name} and my mis is {self.mis} ,I am from {self.city}")


a=details("Rajveer",612511043,"Nagpur")
print(a.name)
print(a.mis)
print(a.city)

c="Rajveer-612511043-Nagpur"
b=details.fromstr(c)
b.show()