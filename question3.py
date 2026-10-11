#search word "learning" exist in the "practice.txt" file


f = open("practice.txt", "r")
data = f.read()
word = "learning"
if (data.find(word) != -1):
    print("found")
else:
    print("Not found")