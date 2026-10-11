#write function that takes two integers a and b and prints all number between them

def print_number(a,b):
    for i in range (a,b+1):
        if i % 2 == 0:
            print(i)        
a = int(input("enter first number: "))
b = int(input("enter second number: "))
print_number(a,b)