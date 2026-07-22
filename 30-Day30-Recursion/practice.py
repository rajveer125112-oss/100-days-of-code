#Factorial

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))

#Fibonacci
# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....
def f(n):
    if n<=1:
        return n
    return f(n-1)+f(n-2)

for i in range(10):
    print(f(i), " ")