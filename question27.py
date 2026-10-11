#WA function to find the factorial of n ( ni is gthe parameter)

def fac(n):
    sum = 1
    for i in range(1,n+1):
        sum *=i
    print("factorial:", sum)

fac(5)
