#change all the occurence of java with python

f = open("practice.txt", "r")
data = f.read()

new_data= data.replace("java", "python")
print(new_data)