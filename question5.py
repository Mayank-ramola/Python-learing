with open("number.txt","r") as f:
    data = f.read()
    print(data)
    print(type(data))    

    # num =""
    # for i in range(len(data)):
    #     if (data[i] == ","):
    #         print(int(num))
    #         num=""
    #     else:
    #         num+=data[i]
    count =0
    nums = data.split(",")
    for val in nums:
        if(int(val)%2 ==0):
            count +=1


print(count)            