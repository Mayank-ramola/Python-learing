#A class method is bound to the class and receives the class as an implicit first argument 
#staticmethod can not access or modify class state and generally for utility

class Person:
    name ="Anonomous"

    @classmethod
    def changename(cls,name):
        cls.name = name


p1 = Person()
p1.changename("Mayank")
print(p1.name)
print(Person.name)