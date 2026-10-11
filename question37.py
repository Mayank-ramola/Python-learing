#write a function to return the sum of digits of a number n

def sum_of_digits(n):
    sum = 0
    for digit in str(n):
        sum  += int (digit)
    return sum
n = int(input("enter a number:"))
print(sum_of_digits(n))