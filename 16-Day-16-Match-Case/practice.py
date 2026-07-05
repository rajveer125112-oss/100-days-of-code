x=int(input("Enter the value of x ="))

match x:
    case _ if x%2==0:
        print("The number is even")
    case _ if x%2!=0:
        print("The number is odd")
    case 87:
        print("the number is 87")

#if earlier case is satisfied then next case won't be satisfied case _ is defined as default or empty case and case (some no.) means it refers to case where x=(some number),we can also use if commands as displayed