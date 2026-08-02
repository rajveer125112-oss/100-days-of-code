def greet(f):
    def mf(*args,**kwargs):                         #mf is used to wrap the function around greetings
        print("Good Morning")
        f(*args,**kwargs)                           #We add *args and **kwargs as we don't know that our function f() will pass how many arguements in this case its two but if I create another function that passes 3 values and we dont use args and kwargs and use a and b instead, it won't work
                                                     #We use *args for multiple values and **kwargs for dictionary values/assigned values.
        print("Thank u for using this function")
    return mf


@greet                                              #calling greet and adding add function so it acts as f()
def add(a,b):
    print(a+b)

add(1,2)                                            #using f()

@greet                                              #Example why we use *args
def add(a,b,c,d):
    print(a+b+c+d)

add(1,2,3,4)

@greet                                              #Example of use of **kwargs
def details(Name="Rajveer",City="Nagpur"):
    print(f"My name is {Name} ,I live in {City} city")

details(Name=input("Enter NAME "),City=input("Enter city "))