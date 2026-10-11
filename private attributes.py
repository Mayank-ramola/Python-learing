 #private attributes and methods are meant to be used only within the class and are not accessible from outside the class

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass   #private like

# acc1 = Account("12233", "15346") 
# print(acc1.acc_no)
# print(acc1.__acc_passs)       





class Person:
    __name = "Mayank"

    def __hello(self):
        print("Hello ")

    def welcome(self):
        self.__hello()   #to print or accesss private like attributes
        


p1 = Person()
print(p1.welcome())