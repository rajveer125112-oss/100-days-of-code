x=int(input("Enter the value of x ="))

match x:
    case _ if x%2==0:
        print("The number is even")
    case _ if x%2!=0:
        print("The number is odd")
    case 87:
        print("the number is 87")