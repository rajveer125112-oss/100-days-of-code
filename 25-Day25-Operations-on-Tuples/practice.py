tuple1=("Japan","Spain","Mexico","India","Beligium")

#Convert tuple to list for modification
t1=list(tuple1)
t1.append("Russia")
t1.pop(2)
t1[3]="America"

#After modification convert it back to tuple(new)

countries=tuple(t1)

print(countries)

#Tuple methods limited as it is immutable

tuple2=(1,22,22,23,23,23,24,24,24,24,24,25,25,26,26)

#For counting number of elements in a tuple
print(tuple2.count(23))

#For printing index number of specified item

mm=tuple2.index(22)

print(mm)
