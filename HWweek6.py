from math import sqrt
class Triangle():    
    def __init__(self, length1, length2, length3):
        self.length1 = length1
        self.length2 = length2
        self.length3 = length3

    def surf_equal(self):
        return self.length1**2*(sqrt(3))/4

       

class Rectangle():
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return(self.length * self.width)

    def perimeter(self):
        return(2*(self.length + self.width))
    
class Square(Rectangle):
    def __init__(self, length):
      super().__init__(length,length)

class Cube(Square):
    def __init__(self, length):
        super().__init__(length)

    def cube_area(self):
         return super().area()*6

    def cube_vol(self):
        return self.length*super().area()

class Pyramid(Square,Triangle):
    def __init__(self,length,length1,hight):
        Square.__init__(self,length)
        self.hight=hight
        Triangle.__init__(self,length1,length1,length1)

    def p_sur_area(self):
        return super().area()+self.triangle.surf_equal()

    def p_vol(self):
        return super().area()*self.hight/3


p =Pyramid(5,6,6)
print(p.surf_equal())
print(p.p_vol())


