

a=input("Enter the value of a")

try:
    for i in range(1,11):
        print("Table of a =",int(a)*i)
except ValueError:                                              #Error when Value data type is correct but something is wrong with the input
    print("The number is not an integer")



b=[1,2,3,4]

try:
    c=b[int(input("Enter index to be printed"))]
    print(c)
except IndexError:                                              #Error when enter value is out of index
    print("The number does not exist in the list  b")