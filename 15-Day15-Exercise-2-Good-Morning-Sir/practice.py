hours=int(input("Enter hours :"))
minutes=int(input("Enter minutes :"))
seconds=int(input("Enter seconds :"))

timeframe=input("Enter AM or PM =")

if timeframe=="AM":
    print("Good morning")

elif timeframe=="PM" and hours==12 :
    print("Good afternoon")

elif timeframe=="PM" and hours<6:
    print("Good afternoon")

elif timeframe=="PM" and hours>6:
    print("Good evening")