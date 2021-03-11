#==========================Triangle and Rectangle========================================0
#Create a class named Triangle and Rectangle.
#Create a subclass named Square inherited from Rectangle.
#Create a subclass named Cube inherited from Square.
#Create a subclass named Pyramid multiple inherited both from Triangle and Square.
#Two dimensional classes (Triangle, Rectangle and Square) should have:
#its dimensions as attributes.(can be inherited from a superclass)
#methods which calculate its area and perimeter separately. Three dimensional classes (Cube and Pyramid) should have:
#its dimensions as attributes which are inherited from a superclass
#its extra dimensions if there is. (hint: maybe for Pyramid)
#methods which calculate its volume and surface area separately. (surface area is optional, you may not do this)
from math import sqrt
#========================================================================================================== parent class
class Rectangle:
    def __init__(self,width,lenght):
        self.width=int(width)
        self.lenght=int(lenght)
    def area_r(self):#---------------------------------------------------------------------------------area computation
        self.area_rectangle = self.width * self.lenght
        print("Area of the rectangle is: {}".format(self.area_rectangle))
        return self.area_rectangle
    def perimeter_r(self):#-----------------------------------------------------------------------perimeter computation
        self.perimeter_rectangle=2*self.width+2*self.lenght
        print("Perimeter of the rectangle is: {}".format(self.perimeter_rectangle))
        return self.perimeter_rectangle
#-------------------------------------------------------------------------------------------------------------sub class
class Square(Rectangle):
    def __init__(self,edge):
        super().__init__(edge,edge)
        self.edge=edge

    def area_suq(self): #-------------------------------------------------------------------------------area computation
        self.area_square=Rectangle.area_r(self)
        print("Area of the square is: {}".format(self.area_square))
        return self.area_square
#-------------------------------------------------------------------------------------------------------inherited class
class Cube(Square):
    def __init__(self,edge):
        super().__init__(edge)
        self.edge=edge

    def volume_c(self):#----------------------------------------------------------------------------volume computation
        self.volume_cube=Rectangle.area_r(self)*self.edge
        print("Volume of the cube is: {}".format(self.volume_cube))
        return self.volume_cube
    def surface_c(self):
        self.surface_cube=Rectangle.area_r(self)*6
        print("Surfac area of the cube is: {}".format(self.surface_cube))
        return self.surface_cube
#=========================================================================================================== main class
class Triangle:
    def __init__(self,edge_bottom,height, edge_2, edge_3):
        self.edge_bottom=edge_bottom
        self.height=height
        self.edge_2=edge_2
        self.edge_3=edge_3
    def area_t(self): #---------------------------------------------------------------------------------area computation
        self.area_triangle=self.height* self.edge_bottom/2
        print("This is a triangle and its area  is: {}".format(self.area_triangle))
        return self.area_triangle
    def perimeter_t(self):
        self.perimeter_trangle=self.edge_bottom+self.edge_2+self.edge_3
        print("The perimeter of triangle is: {}".format(self.perimeter_trangle))
        return self.perimeter_trangle
#-----------------------------------------------------------------------------------------------------inherited class
class pyramid(Triangle,Square):

    def __init__(self,taban_dimension,surface_height,edge): #piramid yuzey ucgen taban 12, piramid yuzey ucgen yukseklık 8, piramid kenar 10
        Triangle.__init__(self,taban_dimension,surface_height,edge,edge)
        Square.__init__(self,taban_dimension)
        self.taban=taban_dimension
        self.height=surface_height
        self.edge1=edge
        self.edge2=edge

    def surface_area_p(self): #-------------------------------------------------------------------------area computation
        self.surface_area_pyramid=Triangle.area_t(self)*4+Square.area_r(self)
        print("The surface of pyramid is: {}".format(self.surface_area_pyramid))
        return self.surface_area_pyramid

    def volume_p(self): #----------------------------------------------------------------------------volume computation
       height_pyramid_sq=(self.height**2-(self.taban/2)**2)
       height_pyramid=sqrt(height_pyramid_sq)
       self.volume_pyramid=height_pyramid*Square.area_suq(self)/3
       print("The volume of pyramid is: {}".format(self.volume_pyramid))
       return self.volume_pyramid
#=======================================END==============================================================================
#=====================================OUTPUT===========================================================================
#This is a triangle and its area  is: 48.0
#Area of the rectangle is: 144
#The surface of pyramid is: 336.0
#Area of the rectangle is: 144
#The volume of pyramid is: 761.9763775866021