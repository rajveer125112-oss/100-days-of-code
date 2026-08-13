class Student:
    def __init__(self,name,mis,branch):
        self.name=name
        self.mis=mis
        self.branch=branch
class Extracurricular(Student):
    def __init__(self, name,mis,branch,hobbies,achievements):
        super().__init__(name,mis,branch)
        self.hobbies=hobbies
        self.achievements=achievements

    def show(self):
        print(f"My name is {self.name} ,my mis is {self.mis}, my branch is {self.branch} \n my hobbies are {self.hobbies} and my achievements are {self.achievements}")



a=Extracurricular("Rajveer",612511043,"Metallurgy","Motion Graphics","Academic excellence award")