class details:
    city="Pune"         #class variable defined for whole class and will not change unless and until a instance is created
    candidate=0
    def __init__(self,name):
        
        
        self.name=name
        self.mis=129310309
        details.candidate+=1
   
    def show(self):
        print(f"My name is {self.name} and my mis is {self.mis} from {self.city} with candidate number {self.candidate} ")


a=details("Harry")
a.show()







b=details("Rajveer")
b.mis=261230119         #Instance variable -- you can change it for any particular
b.city="Mumbai"
b.show()