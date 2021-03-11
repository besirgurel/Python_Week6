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
from Triangle_and_Rectangle import Rectangle,Triangle,Square,Cube,pyramid

print(""" 
1>>>Rectangle
2>>>Square
3>>>Cube
4>>>Triangle
5>>>Pyramid
    """)
choice=input('What do you want to calculate?>>>')
if choice=='1':
    width=int(input('Enter the width of your rectangle>>'))
    lenght=int(input('Enter the lenght of your rectangle>>'))
    l1=Rectangle(width,lenght)
    l1.area_r()
    l1.perimeter_r()
elif choice=='2':
    edge = int(input('Enter the width of your square>>'))
    l2=Square(edge)
    l2.area_suq()
    l2.perimeter_r()
elif choice=='3':
    dimention = int(input('Enter one dimention of your cube>>'))
    l3=Cube(dimention)
    l3.volume_c()
    l3.surface_c()
elif choice=='4':
    bottom = int(input('Enter one bottom edge of your triangle>>'))
    height = int(input('Enter height of your triangle>>'))
    edge_2 = int(input('Enter edge-2 of your triangle>>'))
    edge_3 = int(input('Enter edge-3 of your triangle>>'))
    l4=Triangle(bottom,height,edge_2,edge_3)
    l4.area_t()
    l4.perimeter_t()
elif choice=='5':
    bottom_dimention =int(input('Enter bottom_dimention of your triangle>>'))
    height_surface = int(input('Enter height_surface of your pyramide>>'))
    surfaced_edge_dimention = int(input('Enter surfaced_edge_dimention of your pyramid>>'))
    l5=pyramid(bottom_dimention,height_surface,surfaced_edge_dimention) #piramid yuzey ucgen taban 12, piramid yuzey ucgen yukseklık 8, piramid kenar 10
    l5.surface_area_p()
    l5.volume_p()
else:
    print('Enter all the geometric values correctly!')
print('Sorry for unnecessary information, take you need, dont care others :)')
#========================END==========================================
