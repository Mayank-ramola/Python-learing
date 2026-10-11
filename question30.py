#Write a recursive function to calculate the sum of first n natural numbers

# def nat(n):
#     sum =0
#     for i in range(1,n+1):
#         sum +=i
        
#     print("Total sum:",sum)
    

# number = int(input("Enter the number :"))
# print(nat(number))

def nat(n):
    if(n ==0):
        return 0
    return nat(n-1) + n

number = int(input("Enter the number :"))
print(nat(number))    