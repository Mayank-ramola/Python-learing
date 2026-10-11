#search for number x in this tuple using loop


tup = (1,4,9,16,25,36,49,64,81,100)
print(type(tup))

for num in tup:
    if num == 36:
        print("number found", num)
        break
    else:
        print(num)