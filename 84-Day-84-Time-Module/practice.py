import time

def forl():
    for i in range(10000):
        print(i)

def whilel():
    j=0
    while j<1000:
        j=j+1
        print(j)

init=time.time()
forl()
t1=(time.time()-init)
whilel()
t2=(time.time()-init)

print(t1)
print(t2)

time.sleep(3)
print("For loop wins")

print(time.strftime("%H:%M:%S"))