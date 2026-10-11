#create a new file "practice.txt" using python. 

f = open("practice.txt", "w+")
data = f.write("Hi everyone\nwe are learning  File I/O \nusing java\nI like programming in java.")
f.read()
print(data)
