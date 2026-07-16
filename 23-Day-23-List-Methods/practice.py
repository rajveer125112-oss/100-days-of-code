list1=[1,3,5,34,2,5464,643,23,352,1,1,1,1]

list1.sort()

print(list1)

list1.sort(reverse=True)

print(list1)

list1.append(89)

print(list1)

print(list1.count(1))

list1.insert(1,233)

print(list1)

list2=[23,435,452,3421,"Hellow"]

x=list1+list2

print(x)

list1.extend(list2)

print(list1)

list3=list1.copy()

print(list3)

print(list1.index(2))
