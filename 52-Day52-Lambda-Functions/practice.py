square=lambda x:x**2
cube=lambda x:x**3
print(square(2))
print(cube(2))

def f(fx,val):
    return 10 +fx(val)

print(f(square,2))

