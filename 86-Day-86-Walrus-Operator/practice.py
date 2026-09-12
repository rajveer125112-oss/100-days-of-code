a=True
print(a)
print(a:=False)

numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:  #asking the user inside the condition so that there is no more lines to add 
    print(numbers.pop())


foods=[]

while(food:=input("Enter the food you like "))!="quit":
    foods.append(food)

print(foods)