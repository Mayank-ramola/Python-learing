#Recursion : when a function call itself repeatedly,

def show(n):
    a = 50
    if (n == 0):          #base case
        return
    print(n)
    show(n-1)

show(2 )    

def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return fact(n-1) * n
    
    
number = int(input("Factorial of number :"))
print(fact(number))