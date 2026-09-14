from functools import lru_cache

import time
@lru_cache(maxsize=None)
def f(x):
    time.sleep(5)
    return x**2



print("Square of 2 =",f(2)) #Cache is generated on the spot tell for what input what is the output

print("Square of 3 =",f(3))

print("Square of 4 =",f(4))

print("Square of 2 =",f(2)) #Using Cache we get output instantaneously

print("Square of 3 =",f(3))

print("Square of 4 =",f(4))

#Only use when values are limited or gonna repeat input values ,as cache consumes memory