#Abstraction: hiding the implementation details of a class and only showing the essential features to the user.

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch =False

    def start(self):
        self.acc = True
        self.clutch = True
        print("car started....")    

car1 = car()
car1.start()