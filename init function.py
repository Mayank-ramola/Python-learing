#init function: constructor; All classes have a finction called _init_() , which is always executed when the class is being initiated.

class car:

    def __init__(self, brandname):      #init function
        self.name = brandname
        print("adding car info in database...")

s1 =  car("BMW")
print(s1.name)

s2 = car ("Audi")
print(s2.name)