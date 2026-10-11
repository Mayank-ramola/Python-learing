#Methods that don't use the self parameter (work at class level)

class students:
    @staticmethod
    def hello():
        print("hello world")

s1 = students
s1.hello()