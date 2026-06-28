#Before typecasting

a="44"
b=44

print(type(a),type(b))

#Adding them by externally typecasting a as string and integer cannot be added

print(int(a)+b)

#This was external typecasting

#Internal Typecasting

c=91
d=32.1

print(c+d)
print(type(c+d))