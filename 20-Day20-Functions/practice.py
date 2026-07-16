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


def mus(numbers):
    total=1
    for x in numbers:
        total = total*x
    return total

print(mus((1,2,3)))


rev=""
def reverse(string):
    rev=""
    len1=len(string)
    while len1>0:
        rev=rev+string[len1-1]
        len1=len1-1
    return rev


print(reverse("hello"))

def factorial(k):
    fact=1
    while k>0:
        fact=fact*k
        k=k-1
    return fact
        

print(factorial(12))


def checkrange(x,y):
        v=int(input("enter the numero ="))
        if v<=y and v>=x:
            print("number is in range")
        else:
            print("number is not in range")

checkrange(1,16)

def upperlower(string:str):                     #I learned basics of string methods in college
    n=0
    m=0
    for char in string:
        if char.isupper()==True:
            n=n+1
        elif char.islower()==True:
            m=m+1
    print("Number of upper cased letters ",n)
    print("Number of lower cased letters ",m)
 
upperlower("HEllo")


def even(*numbers):                             #I learned how to push multiple arguments using * and some list methods in college
    enim=[]
    for num in numbers:
        if num%2==0:
            enim.append(num)
    return enim
print(even(1,2,3,4,6,8))