#Write a function that prints the digit of a number , n

def print_digits(n):
    for digit in str(n):
        print(digit)
digit = int(input("Enter a number: "))
print_digits(digit)        