class Shape:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return self.radius**2

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)

    def area(self):
        return 3.14 * super().area()
    
a = Circle(5)
print(a.area())
