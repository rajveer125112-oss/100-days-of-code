dict1={'name':'Rajveer','age':19,'eligible':True}


dict1.update({'age':19.5})
print(dict1)

dict1.clear()
print(dict1)

dict2={'name':'Rajveer','age':19,'eligible':True}

dict2.pop('eligible')
print(dict2)

dict2.popitem()
print(dict2)
