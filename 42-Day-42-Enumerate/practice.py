list1=[2023,2024,2025,2026]
n=int(input('Where to start'))
m=0
for index,year in enumerate(list1,start=n):
  
        m=m+year

        if index==2:
                print("2025")
        else:
                print("Nice")

print(m)


