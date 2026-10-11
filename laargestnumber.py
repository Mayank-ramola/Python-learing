# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))


# if a > b :
#     print("A is largest number")
# else:
#     print("B is largest number")    

list = [54,36,45,87,50]
largest = list[0]

for num in list:
    if num > largest:
        largest = num

print(largest," is the largest number" )        