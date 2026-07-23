

try:
    a=int(input("Enter the value ="))
except ValueError:
    print("The number is not integer")
else:
    print("The number is integer")
finally:
    print("The program executed successfully")
