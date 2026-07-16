list1=[1,2,3,4,5,6,True,False,"Hellow",23.4342]


print(list1[0:3])
print(list1[:3])
print(list1[-4:-1])
print(list1[-1])
print(list1[len(list1)-1])
print(list1[2:4])


for x in list1:
    if type(x)==bool:
        print("Its a boolean ")
    else:
        print("Its not a boolean")
list2=["Hi","Hellow","GoodMorning"]
even=[i for i in list2 if len(i)>2 ] #list comprehension
even2=[i for i in list2 if "H" in i]
print(even)
print(even2)