import time
timestamp1 = time.strftime('%H:%M:%S')
print(timestamp1)

n=input("Enter AM or PM =")
timestamp2 = int(time.strftime('%H'))
if n=="AM":
    print("Good Morning")
elif n=="PM" and timestamp2<=17:
    print("Good Afternoon")
elif n=="PM" and timestamp2>=18:
    print("Good evening")

