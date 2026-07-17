tuple1=(2,3,4,5,"Hello",True,"India")


print(tuple1[0:4])  #Indexing
print(tuple1[:4])
print(tuple1[-2])

if 2 in tuple1:     #Checking for elements in tuple
    print("Yes")
else:
    print("No")     

if 23 in tuple1:    #Checking for elements in tuple
    print("Yes")
else:
    print("No")

print(tuple1[0:6:2]) #with step 2