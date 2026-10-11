#WAP to find the factorial of first n numbers (using for )

n = int(input("Enter number:"))
sum = 1

for i in range(1,n+1):
    sum *=i
    
print("factorial is:", sum)    