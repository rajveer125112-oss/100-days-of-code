import os



m=os.listdir("test")


for i,f in enumerate(m,start=1):
    os.rename("test/"+f,"test/"+f"{i}.jpg")

