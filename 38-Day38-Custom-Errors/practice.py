a=int(input("Enter the value between 11 and 19 ="))

if a<11 or a>19:
    raise ValueError("a is not between 11 and 19")
else:
    print("The value is between 11 and 19")



class Myerror(Exception):
    pass
try:
        b=[23,24,25,26]
        i=int(input("Enter the value of index ="))
        if i<0 or i>3:
             raise Myerror()                            #Custom errors only run when we raise them as python doesn't know Myerror
        print(b[i])
except Myerror :
     print("The wrong index is entered")
    