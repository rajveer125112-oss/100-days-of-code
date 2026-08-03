class details:
    def __init__(self,name,mis,city):
        self._name=name
        self._mis=mis
        self._city=city

    def information(self):
        print(f"I am {self._name} from {self._city} and mis {self._mis}")

    @property
    def info(self):
            print(f"I am {self._name} from {self._city} and mis {self._mis}")

    @info.setter
    def info(self,value):
        name1,mis1,city1=value
        self._name=name1
        self._mis=mis1
        self._city=city1



a=details('Rajveer','93142231','Nagpur')
a.info=('Ram','64468463','Kanpur')

a.information()