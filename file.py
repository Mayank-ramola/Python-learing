f = open("demo.txt", "w")
data = f.write(str("hello world"))
f.close()

#other metthod 

with open ("demo.txt","r") as f:
    data = f.read()
    print(data)


#Deleting file
import os

os.remove ("demo.txt")