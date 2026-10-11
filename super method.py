#super method is used to acess methods of parent class

class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("cae started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):
    def __init__(self, name , type):
        super().__init__(type)         #parent --  super method
        self.name = name


car1 = ToyotaCar("prius", "electic")
print(car1.type)