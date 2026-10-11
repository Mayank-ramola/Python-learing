#Inheritance : When one class (child/deerived) derives the properties and method of another class (parent/base)
#single inheritence type
# class Car:
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stoped..")    

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")

# print(car1.start())
# print(car1.stop())



#Multi-level inheritence

# class Car:
#     @staticmethod
#     def start():
#         print("Car is started..")

#     @staticmethod
#     def stop():
#         print("Car is stopped..")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type = type        

# car1 = Fortuner("disel")
# print(car1.start())        


#Multiple inheritence

class A:
    val1 = "welcome to class A"

class B:
    val2 = "welcome to class B"

class c(A,B):
    val3 = "welcome to class C"

c1 = c()
print(c1.val1)
print(c1.val2)
print(c1.val3)
