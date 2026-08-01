f=open("test.txt","r")
while True:
    t=f.readline()
    if not t:
        break
    print(t)
f.close()



f=open("test.txt","w")
lines=["Life\n","Death\n","Birth\n"]
l=f.writelines(lines)
f.close()
print(l)

f=open("test.txt","w")

lines1=["Live","Die","Born"]

for line in lines1:
    n=f.write(line +'\n')

f.close()
