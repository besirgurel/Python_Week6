"""Create a class named Triangle and Rectangle.

Create a subclass named Square inherited from Rectangle.

Create a subclass named Cube inherited from Square.

Create a subclass named Pyramid multiple inherited both from Triangle and Square.

Two dimensional classes (Triangle, Rectangle and Square) should have:

its dimensions as attributes.(can be inherited from a superclass)
methods which calculate its area and perimeter separately. Three dimensional classes (Cube and Pyramid) should have:
its dimensions as attributes which are inherited from a superclass
its extra dimensions if there is. (hint: maybe for Pyramid)
methods which calculate its volume and surface area separately. (surface area is optional, you may not do this)"""

######################################################################################################################


class Rectangle:
    def __init__(self, a, b):
        self.side_1 = a
        self.side_2 = b
        
    def rec_area(self):
        area_rec = self.side_1 * self.side_2
        print(f"Area of the Rectangle: {area_rec}")         
        return area_rec 
        
    def rec_perimeter(self):
       perimeter_rec = (self.side_1 + self.side_2) * 2
       print(f"Perimeter of the Rectangle: {perimeter_rec}")
       return perimeter_rec
      
class Triangle(Rectangle):
    def __init__(self,a , b , c, h):
        Rectangle.__init__(self,a,b)
        self.side_3 = c
        self.height  = h
        
    def tri_area(self):
        area_tri = (self.side_3 * self.height)/2
        print (f"Area of the Triangle: {area_tri}")
        return area_tri
    
    def tri_perimeter(self):
        perimeter_tri = self.side_1 + self.side_2 + self.side_3
        print (f"Perimeter of the Triangle: {perimeter_tri}")
        return perimeter_tri    

class Square(Rectangle):
    def __init__(self, a):
        Rectangle.__init__(self, a, a)
        
    def squ_area(self):
        self.alan=self.side_1 ** 2
        print (f"Area of the Square: {self.alan}")
        return self.alan
    
    def squ_perimeter(self):
        perimeter_squ = 4*self.side_1
        print (f"Perimeter of the Square: {perimeter_squ}")
        return perimeter_squ
        
class Cube(Square):
    def __init__(self, a):
        Square.__init__(self, a)
        
    def cub_volume(self):
        area_squ = super().squ_area()
        print(f"Volume of Cube: {area_squ * self.side_1}")
        
    def squ_area(self):
        area_squ = super().squ_area()
        print(f"Area of the cube: { area_squ * 6}")
    
      
class Pyramid(Triangle, Square):                        
    def __init__(self, a, b, c,h):
        Triangle.__init__(self,a,b,c,h)
        Square.__init__(self,a)       
        
    def squ_pyramid_volume(self):
        super().squ_area()
        pyramid_volume = (self.alan * self.height)/3
        print (f"Volume of Cube:{pyramid_volume}")
        
    def squ_pyramid_surface_area(self):
        surface_area = self.side_1 + (self.side_1**2 + 4*self.height)**1/2
        print (f"Surface area of Pyramid:{surface_area}")  
           
   

Rec1=Rectangle(3,5)
Triangle_1=Triangle(5,10,15,20)

Pyramid_1 = Pyramid(2,3,4,5)
Pyramid_1.squ_pyramid_surface_area()
print("--------------------------")
Square_1=Square(3)
print(Square_1.squ_area())
print("---------------------------")
cub_1=Cube(5)
cub_1.squ_area()
cub_1.cub_volume()
print("---------------------------")
pyrmd_1=Pyramid(2,3,4,5)
pyrmd_1.squ_pyramid_volume()

