#class attributes: class.attr

class students:
    college_name = "AKIT"              #class attributes

    def __init__(self, name , marks ):
        self.name = name               #object attributes
        self.marks = marks             #object attributes
        print("Adding new student info in database...")

s1 =students("Mjiksnk",90)
print(s1.name, s1.marks,s1.college_name)        

s2 =students("Kjuubj",90)
print(s2.name, s2.marks,s2.college_name)