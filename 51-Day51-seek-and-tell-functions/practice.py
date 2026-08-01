with open("test.txt","w") as f:
    f.write("Hellow world this is a nice place to have fun")


with open("test.txt","r") as f:
    f.seek(10)
    print(f.tell())
    d=f.read(5)
    print(d)

with open("Nice.txt","w") as n:
    n.write("Hellow Im feeling good todayy")
    n.truncate(5)
    