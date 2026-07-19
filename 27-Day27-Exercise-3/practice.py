def ans(i,j):
    n=0
    if j==answers[i]:
            print("Answer is correct")
            n=n+1000*(i+1)
            print("You won",n,"rupees")
    else:
          print("Answer is incorrect")
        






answers=["A","B","C","D"]

q1=["Which Indian city is famously known as the \"Orange City\"?","A. Nagpur","B. Nashik","C. Bhopal","D. Indore",]
print("The first question is :",q1[0])
print(q1[1])
print(q1[2])
print(q1[3])
print(q1[4])

ans(0,input("Enter the answer ="))
      
     

q2 = [
    'Which state is known as the "Spice Garden of India"?',
    "A. Karnataka",
    "B. Kerala",
    "C. Andhra Pradesh",
    "D. Tamil Nadu",
]

print("The second question is :",q2[0])
print(q2[1])
print(q2[2])
print(q2[3])
print(q2[4])

ans(1,input("Enter the answer ="))
n=0
while n<2:
    m=0
    if ans(n,input("Enter the answer ="))=="Answer is correct":
          m=m+1000
          print("You won total of",m,"rupees")
    n=n+1






     


