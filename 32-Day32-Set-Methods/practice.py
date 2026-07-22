set1={1,2,3,4,"Hellow",True,12.34}

set2={1,2,3,4,99,99,111,343,"Hellow"}

#Sets cannot be added normally using "+" like lists and tuples

set4=set1.union(set2)           #new set is returned
print(set4)

set1.update(set2)
print(set1)                     #Updates set1

set11={12,232,43,12312,434,54252}
set12={213,3413,452,12,232,134}
set5=set11.intersection(set12)    #new set is returned
print(set5)

set11.intersection_update(set12)
print(set11)                     #set is updated

set23={1,2,3,4,22,34,55,66,77,88,99}
set24={1,2,3,4,534,6,53,}
set6=set23.symmetric_difference(set24)    
print(set6)                     #A new set with excluding the common items in both sets is returned

set23.symmetric_difference_update(set24)
print(set24)                     #Set 1 is updated with items that are found in either sets not in both

set25={23,241,3512,352,132,1241}
set26={214,3145,3142,312334,213,23,241,"Hello"}

set27=set25.difference(set26)
print(set27)                    #Creates a set where values from the other sets that are present in first set are removed

set25.difference_update(set26)
print(set27)                    #Updates Set and removes duplicate values from other sets


cities={"Nagpur","Mumbai","Pune"}
countries={"India","Japan,","Germany"}
print(cities.isdisjoint(countries)) #returns true if sets do not have common elements

print(cities.issuperset(countries))

a={122123,2144124,2312,21334}
b={2312,21334}

print(b.issubset(a))

a.add("Hello")
print(a)

a.remove("Hello")
print(a)

a.discard("Hellow")         #No error raised
print(a)

a.pop()
print(a)
print(a.pop())



b.clear()

print(b)

cities={"Mumbai","Nagpur","Pune"}

if "Nagpur" in cities:
    print("Nagpur is an orange city")
else:
    print("Cities")