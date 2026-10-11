#reverse without using slicing

a = "helloworld"

rev = ""
for i in a:
    rev = i + rev
print(rev)    
print("---------------------------")

b = "another"
i = len(b)-1

while i >= 0:
    print(b[i], end = "")
    i -=1