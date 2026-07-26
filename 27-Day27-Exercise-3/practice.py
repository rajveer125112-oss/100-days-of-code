class Incorrectans(Exception):
    pass
    
def ans(i,j):
        price=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
        answers=["A","B","B","A","C","A","C","D","B","B"]
        m=input("Enter your decision =Sure/Quit = ")
     
        pass
        
        try:
            if j==answers[i]:
                print("Answer is correct")
                                                   
                print("You won",price[i],"rupees")    

            elif j!=answers[i]:
                
                raise Incorrectans("Incorrect answer")  
    

        except Incorrectans:
            if m=="Sure":
                
                if i in range(0,4):
                    print("Answer is incorrect","Your total won price is =",0)
                elif i in range(4,9):
                     print("Answer is incorrect","Your total won price is =",10000)
                elif i==9:
                     print("Answer is incorrect","Your total won price is =",320000)
            elif m=="Quit":
                print("Your total won price is =",price[i-1])
                     
            exit()
            
    
   
        

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


q3 = [
    'Which monument was built by Emperor Shah Jahan in memory of his wife Mumtaz Mahal?',
    "A. Qutub Minar",
    "B. Taj Mahal",
    "C. Red Fort",
    "D. Hawa Mahal",
]

print("The third question is :",q3[0])
print(q3[1])
print(q3[2])
print(q3[3])
print(q3[4])

ans(2,input("Enter the answer ="))

q4 = [
    'Which of these chemical elements is named after the creator of the periodic table?',
    "A. Mendelevium",
    "B. Einsteinium",
    "C. Nobelium",
    "D. Rutherfordium",
]

print("The fourth question is :",q4[0])
print(q4[1])
print(q4[2])
print(q4[3])
print(q4[4])

ans(3,input("Enter the answer ="))

q5 = [
    'In India, the highest peacetime gallantry award is known by which name?',
    "A. Param Vir Chakra",
    "B. Maha Vir Chakra",
    "C. Ashok Chakra",
    "D. Kirti Chakra",
]

print("The fifth question is :",q5[0])
print(q5[1])
print(q5[2])
print(q5[3])
print(q5[4])

ans(4,input("Enter the answer ="))

q6 = [
    'Which planet in our solar system has the highest number of moons?',
    "A. Jupiter",
    "B. Saturn",
    "C. Uranus",
    "D. Neptune",
]

print("The sixth question is :",q6[0])
print(q6[1])
print(q6[2])
print(q6[3])
print(q6[4])

ans(5,input("Enter the answer ="))

q7 = [
    'Who is the author of the famous historical book "Discovery of India"?',
    "A. Mahatma Gandhi",
    "B. Rabindranath Tagore",
    "C. Jawaharlal Nehru",
    "D. Dr. B.R. Ambedkar",
]

print("The seventh question is :",q7[0])
print(q7[1])
print(q7[2])
print(q7[3])
print(q7[4])

ans(6,input("Enter the answer ="))

q8 = [
    'Which of these organs is responsible for filtering blood and producing urine in the human body?',
    "A. Liver",
    "B. Heart",
    "C. Lungs",
    "D. Kidneys",
]

print("The seventh question is :",q8[0])
print(q8[1])
print(q8[2])
print(q8[3])
print(q8[4])

ans(7,input("Enter the answer ="))

q9 = [
    'The classic Indian dance form "Kathakali" originated in which state?',
    "A. Tamil Nadu",
    "B. Kerala",
    "C. Andhra Pradesh",
    "D. Karnataka",
]

print("The seventh question is :",q9[0])
print(q9[1])
print(q9[2])
print(q9[3])
print(q9[4])

ans(8,input("Enter the answer ="))


q10 = [
    'Which country was the first to implement a Goods and Services Tax (GST)?',
    "A. Canada",
    "B. France",
    "C. Germany",
    "D. Australia",
]

print("The seventh question is :",q10[0])
print(q10[1])
print(q10[2])
print(q10[3])
print(q10[4])

ans(9,input("Enter the answer ="))