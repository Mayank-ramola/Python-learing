#WAP to find the sum of first n natural numbers

n = int(input("times:"))
sum = 0

# n = int(input("Times:"))
# sum = 0
# i =1
# while i <= n:
#     sum += i
#     i +=1
    
# print("total sum=", sum) 


for i in range(1,n+1):
    sum+=i
    
print("total sum:",sum)