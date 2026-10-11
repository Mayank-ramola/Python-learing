#Define a circle class to create a cirlce with radius r using the constructor 
#define a Area() method of the class which claculates the  area of the circle 
#DEfine a perimeter () method of the class which allows you to calculate the perimeter of the circle


class Circle:
    def __init__(self, radius):
        self.radius = radius


    def Area(self):
        return (22/7) * self.radius ** 2
    
    def Perimeter(self):
        return 2 * (22/7) *self.radius

c1 = Circle(21)     

print(c1.Area())
print(c1.Perimeter())

