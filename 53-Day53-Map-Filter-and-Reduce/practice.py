list1=[1,2,3,4,5]

square=lambda x:x**2

doubled=list(map(square,list1))

print(doubled)

condition=lambda x:x>3

conditioned=list(filter(condition,list1))

print(conditioned)

from functools import reduce
add=lambda x,y: x+y
n=reduce(add,list1)
print(n)