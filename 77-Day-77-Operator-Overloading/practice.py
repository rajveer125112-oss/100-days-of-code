class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    def __add__(self,x):
        if self.i==-(x.i) and self.j==-(x.j) and self.k==-(x.k):
            return 0
        else:
            return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    def __sub__(self,y):
        if self.i==y.i and self.j==y.j and self.k==y.k:
            return 0
        else:
            return Vector(self.i-y.i,self.j-y.j,self.k-y.k)
        
    
        


a=Vector(1,2,3)
print(a)

b=Vector(-1,-2,-3)
print(b)

c=a+b
d=a-b
print(c)
print(d)