



c=[111,2222,3333,4444,5555]

def error(*b):
    print("Your total price won is ",sum(b))
n=3
m=[]                                                #Remember
for i in range(n+1):    
    m.append(c[i])

m=tuple(m)
print(error(*m))
