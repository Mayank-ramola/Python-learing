#WAP to finf the greatest of 3 number entered by the user

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))

if(a>b and a>c):
    print("a is the greatest number")
elif(b>a and b>c):
     print("b is the greatest number")
elif(c>a and c>b):
     print("c is the greatest number")