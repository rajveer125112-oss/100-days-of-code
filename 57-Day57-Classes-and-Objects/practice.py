class Details():
    Name="Rajveer Singh Kalsi"
    Mis=9746523331
    College="COEP Pune"
    def info(self):
        print(f"Student {self.Name} is from {self.College} has Mis {self.Mis}") #self is used to define info of a object 

a=Details()
a.Name="Ram"
a.Mis=6566464544
a.College="IIT Kanpur"
a.info()

b=Details()
b.info()

c=Details()
c.Name="John"
c.Mis=186545461
c.info()