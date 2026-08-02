class details():
    def __init__(self,n,m,c):
        self.name=n
        self.Mis=m
        self.College=c

    def info(self):
        print(f"Student {self.name} from {self.College} has Mis {self.Mis}")


a=details("Rajveer",1884651846,"COEP")
b=details("Ram",1845319845,"IIT Kanpur")


a.info()
b.info()