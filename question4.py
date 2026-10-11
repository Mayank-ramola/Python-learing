#Find in which line of the file does the word "learning" occurs first. Print -1 if word not found

def find_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if (data.find(word) !=1):
            print("found")
        else:
            print("-1")

def find_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return

            line_no +=1    

    return -1

find_line()