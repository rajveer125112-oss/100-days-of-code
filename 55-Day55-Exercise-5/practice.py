import random

a=input("Enter your move (snake/water/gun) =")
comp=["snake","water","gun"]

computer=random.choice(comp)
print(computer)

if computer==a:
    print("draw")
elif computer=="snake" and a=="water":
    print("you lost")
elif computer=="snake" and a=="gun":
    print("you win")
elif computer=="water" and a=="snake":
    print("you win")
elif computer=="water" and a=="gun":
    print("you lost")
elif computer=="gun" and a=="snake":
    print("you lost")
elif computer=="gun" and a=="water":
    print("you win")