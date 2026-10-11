#WAP to check if a list contains a palindrome of elements 

list = [4,5,6,5,4]
lis1 = list.copy()
lis2 = lis1.reverse()
if(lis1 == list):
    print("list is plaindrome")
else:
    print("list is not palindrome")