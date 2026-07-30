x=23

def f():
    global x
    x=24
    
    y=25
   
f()                                 #call the function first to change global variable x
print(x)