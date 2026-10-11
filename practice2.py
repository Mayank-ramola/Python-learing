#Define a employee class with attributes role, department and salary. This class has a showDetails() method.
#Create an engineer class that inherits properties from employee and has additional attributes : name and age

class Employee :
    
    def __init__(self, role, department , salary):
        self.role = role
        self.department = department
        self.salary = salary
    
    def showDetails(self):
        print("role = ", self.role)
        print("department = ", self.department)
        print("salary = ", self.salary)


class Engineer (Employee):
    def __init__(self,name, age):
        self.name = name
        self.age = age 
        super().__init__ ("Accountant", "Finance", "50000")

    def showDetails2(self):
        print("name =",self.name)
        print("age =", self.age)          

c1 = Engineer("Anonomous", 25)
c1.showDetails()
c1.showDetails2()