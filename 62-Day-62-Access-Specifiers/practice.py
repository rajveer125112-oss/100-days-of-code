class details:
    def __init__(self,name,mis,city):
        self.name=name
        self.mis=mis
        self.city=city

    def show(self):
        print(f'I am {self.name} from {self.city} with mis {self.mis}')


a=details("Rajveer",1231341344,"Nagpur")            #public

a.show()



class details:
    def __init__(self,name,mis,city):
        self.name=name
        self.__mis=mis
        self.city=city

    def show(self):
        print(f'I am {self.name} from {self.city} with mis {self.__mis}')   


a=details("Rajveer",12240124,"Nagpur")   
print(a._details__mis)                             #accessing mangled variable

a.show()


class details:
    def __init__(self,):
        self.name="Rajveer"
        self.mis=121421234
        self.city="Nagour"

    def _show(self):
        print(f'I am {self.name} from {self.city} with mis {self.mis}')   

class nice(details):
    pass

a=details()
print(a._show())

b=nice()
print(b._show())