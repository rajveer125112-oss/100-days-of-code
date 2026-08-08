class Library:
    numberofbooks=0
    
    def __init__(self):
          self.books=[]
          
          
   
    def operation(self):
        n=5
        while n>0:
            a=input("Book name (enter \"show me number of books\" to stop and see number of books)=")
            self.books.append(a)
            Library.numberofbooks+=1
           
            if a=="show me number of books":
                 break
            n=n+1

    def check(self):
        if self.numberofbooks==len(self.books):
            print(f"Number of books are {self.numberofbooks-1} ")
        else:
            print("Error")
       


a=Library()
a.operation()
a.check()

