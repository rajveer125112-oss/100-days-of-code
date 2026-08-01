a="Hello"           #immutable same memory allocation hence true for a is b
b="Hello"

print(a is b)
print(a==b)

c=[23,24,25]        #Lists are mutable hence two different lists are created
d=[23,24,25]

print(c is d)

print(c==d)