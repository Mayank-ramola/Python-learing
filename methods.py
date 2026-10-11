#Methods are functions that belong to objects

class students:
    college_name = "AKIT"

    def __init__(self, name , marks ):
        self.name = name 
        self.marks = marks
        print("Adding new student info in database...")

    def welcome(self):                #methods
        print("WELCOME STUDENTS...")    

    def get_marks(self):               #methods
        return self.marks

s1 =students("karan",90)
print(s1.name, s1.marks,s1.college_name)
s1.welcome()    
print(s1.get_marks())
