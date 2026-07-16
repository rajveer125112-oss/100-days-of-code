def name(fname="Harry",lname="Larry"):
    print(fname , lname)
name()                                  #Default argurements
name("Sundar")
name("Sundar","Pichai")
name(lname="Pichai",fname="Sundar")     #Keyword arguements



def avg(*numbers):                      #Variable length arguements
    m=sum(numbers)/len(numbers)
    return m                            #returns the value back to calling function

print(avg(1,2,3))

def details(**details):                 #Keyword arbitrary arguements
    print("Details are as follows :", details["Name"], details["Country"],details["Mobilenumber"])


details(Country="India",Name="Rajveer",Mobilenumber=213123)

