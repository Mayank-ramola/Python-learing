#WAP to check if a number entered by the user id odd or even 

num = int(input("Enter the number: "))
rem = num%2
if( rem ==0):
    print("Even number")
else:
    print("Odd number")