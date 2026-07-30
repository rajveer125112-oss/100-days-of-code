f=open("test.txt","r")
m=f.read()

print(m)
f.close()

f=open("test.txt","w")
n=f.write("Hellowww")

f.close()

with open("test.txt","w") as f:
    f.write("This is nice")