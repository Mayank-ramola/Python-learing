#write a function to return the count the number of digit in a number , n

def count_digits(n):
    count = 0
    for digit in str(n):
        count+=1
    return count
n = int(input("enter a number:"))
print("count of digits is ", count_digits(n))