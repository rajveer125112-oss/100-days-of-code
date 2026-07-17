#   Already done at Day15





#Using if-else

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

#Using time module

import time                             #Imported time module

timestamp1 = time.strftime('%H:%M:%S')  #Using .strftime to print local time

print("The current time is ",timestamp1)

n=input("Enter AM or PM =")             #Inputing AM or PM

timestamp2 = int(time.strftime('%H'))   #Converting hour format into integer so that we can compare it with integers for time specific greetings

if n=="AM":                             #If-statement for Good Morning
    print("Good Morning") 
elif n=="PM" and timestamp2<17:         #elif-statement for Good Afternoon
    print("Good Afternoon")
elif n=="PM" and timestamp2>=17:        #elif-statement for Good Evening
    print("Good evening")

