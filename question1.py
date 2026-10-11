#create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print average


class students:

    def __init__(self, name , marks ):
        self.name = name 
        self.marks = marks

        print("Students details are given:")

    def average(self):
        sum = 0
        for i in self.marks:
            sum+= i
        print("yo:", self.name ,"your average is :", self.marks , sum/3)


s1 = students("Mayank", [60,84,78])
print(s1.name , s1.marks)          
s1.average()