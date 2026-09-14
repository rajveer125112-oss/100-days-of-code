def generator():
    for i in range(5000):
        yield i



gen=generator()

print(next(gen))
print(next(gen))
print(next(gen))

#It stores the recipe to generate the values, not the values itself like lists hence less memory is needed and is more fast and efficient than using list

#If I want to print values in sequence:

for g in gen:
    print(g)