def f(x,y):
    mean=(x+y)/2
    print(mean)

f(2,3)
def m(a,b):
    if a>b:
        print("first number is greater than second number")
    elif a<b:
        print("second number is greater than first number")
    elif a==b:
        print("first and second numbers are equal")

m(2,3)

def n(c,d,e):
    print("Maximum of three numbers is ",max(c,d,e))

n(1,2,3)

def mus(numbers):
    total=0
    for x in numbers:
        total = total+x
    return total

print(mus((1,2,3)))

