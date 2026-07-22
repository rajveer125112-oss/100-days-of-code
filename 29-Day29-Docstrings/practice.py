#Docstrings are used to define what a function performs using '''___''' just after defining a function .
#It's not like comments as python treats it specially ,we can call these docstrings to display in output using functionname.__doc__


def function(n):
    '''This function is used to calculate
    the square of the number. We can input the value 
    n and calculate its square easily.'''
    print(n**2)


print(function(12))
print(function.__doc__)

