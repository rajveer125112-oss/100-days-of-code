class Math:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add1(self):
        print(self.a+self.b)
    @staticmethod
    def add(a,b):
        print(a+b)


c=Math(2,3)
c.add1()

c.add(1,44)