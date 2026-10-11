#break used to terminate the loop when encountered
#countinue used to skip the current iteration & countinue execution of the loop with the next iteration

i = 0
while i<=5:
   
    if(i == 3):
        continue
    print(i)
    i+=1

i = 0
while i<=5:
   
    if(i == 3):
        break
    print(i)
    i+=1
