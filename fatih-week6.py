"""Create a class named Triangle and Rectangle.

Create a subclass named Square inherited from Rectangle.

Create a subclass named Cube inherited from Square.

Create a subclass named Pyramid multiple inherited both from Triangle and Square.

Two dimensional classes (Triangle, Rectangle and Square) should have:

    its dimensions as attributes.(can be inherited from a superclass)
    methods which calculate its area and perimeter separately. Three dimensional classes (Cube and Pyramid) should have:
    its dimensions as attributes which are inherited from a superclass
    its extra dimensions if there is. (hint: maybe for Pyramid)
    methods which calculate its volume and surface area separately. (surface area is optional, you may not do this)
"""
import math
class Triangle : 
    def __init__(self, length1, length2, length3, height) : 
        self.length1 = length1
        self.length2 = length2
        self.length3 = length3
        self.height = height
    def perimeter(self) :
        perimeterOfTriangle = self.length1 + self.length2 + self.length3
        return perimeterOfTriangle
    def area(self): 
        areaOfTriangle = self.length1 * self.height / 2 
        return areaOfTriangle
  

class Rectangle :
    def __init__(self, length1, length2) :
        self.length1 = length1
        self.lengt2= length2
    def area (self):
        areaOfRectangle = self.length1*self.length2
        return areaOfRectangle
    def perimeter(self):
        perimeterOfRectangle = 2 * (self.length1 + self.length1) 
        return perimeterOfRectangle
    
class Square(Rectangle) :
    def __init__(self, length1) :
        super().__init__(length1, length1)
    def area (self):
        areaOfSquare = self.length1*self.length1
        return areaOfSquare
    def perimeter (self) :
        perimeterOfSquare  =self.length1 * 4
        return perimeterOfSquare
    
class Cube(Square) :
    def __init__(self, length1):
        super().__init__(length1)
    def volume(self):
        volumeOfCube = self.length1**3
        return volumeOfCube
    def area(self):
        areaOfCube = self.length1*self.length1*6
        return areaOfCube
    def perimeter(self):
        perimeterOfCube = self.length1*12
        return perimeterOfCube
            
class Pyramid(Triangle, Square) :
    def __init__(self, length1, length2, length3, height):
        super().__init__(length1, length2, length3, height)
        
    def volume (self):
        volumeOfPyramid =( self.length1 * self.length1  * self.height) / 3
        return volumeOfPyramid
    def area(self) :
        s = (self.length1 + self.length2 + self.length3) / 2
        areaOfPyramid  = math.sqrt(s*(s-self.length1)*(s-self.length2)*(s-self.length3)) *4 + self.length1**2
        return areaOfPyramid  
    
TRIANGLE = Triangle(6, 7, 8, 10)
print(TRIANGLE.area())
print(TRIANGLE.perimeter())

RECTANGLE = Rectangle(6, 7)
print(TRIANGLE.area())
print(RECTANGLE.perimeter())

SQUARE = Square(5)
print(SQUARE.perimeter())
print(SQUARE.area())

CUBE = Cube(5)
print(CUBE.area())
print(CUBE.perimeter())
print(CUBE.volume())

PYRAMID = Pyramid(5,5,5,5)
print(PYRAMID.area())
print(PYRAMID.volume())

 
    
    
    
    
