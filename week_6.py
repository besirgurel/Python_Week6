from math import sqrt

class Triangle:
    def __init__(self,base_length,edge,edge2,height):
        self.base_length=base_length
        self.edge=edge
        self.edge2=edge2
        self.height=height
    def calculate(self):
        area=self.base_length*self.height/2
        perimeter=self.base_length+self.edge+self.edge2
        return f"Area: {area} Perimeter: {perimeter}"


class Rectangle:

    def __init__(self,a,b):
        self.a=a
        self.b=b
    def calculate(self):
        area=self.a*self.b
        perimeter=2*self.a+2*self.b
        return f"Area:{area} Perimeter: {perimeter}"

class Square(Rectangle):
    def __init__(self,a):
        super().__init__(a,a)
    def calculate_square(self):
        area=self.a**2
        perimeter=self.a*4
        return f"Area:{area} Perimeter: {perimeter}"

class Cube(Square):
    def __init__(self,a):
        super().__init__(a)
    def calculate_cube(self):
        area=(self.a**2)*6
        perimeter=self.a*24
        volume=self.a**3
        return f"Area:{area} Perimeter: {perimeter} Volume: {volume}"

class Pyramid(Triangle,Square):
    def __init__(self,base_length,edge,edge2,height):
        super().__init__(base_length,edge,edge2,height)
    def calculate_pyramid(self):
        area=self.base_length*(self.base_length+((self.base_length**2)+4*(self.height**2))**0.5)
        volume=((self.base_length**2)*self.height)/3
        return f"Area:{area} Volume: {volume}"

a=Triangle(5,12,13,12)
b=Rectangle(10,20)
c=Square(10)
d=Cube(10)
e=Pyramid(5,12,13,12)
print("""Triangle {}
Rectangle {}
Square {}
Cube {}
Pyramid {}""".format(a.calculate(),b.calculate(),c.calculate_square(),d.calculate_cube(),e.calculate_pyramid()))