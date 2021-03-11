### All Rights Reserved ###
'''
Developer: Alper Kaan
Date: 11.03.2021
Purpose of Software: shape(HM6)
'''
#Created by InfotechAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
class Triangle: 
    def __init__(self):
        self.a = int(input("Enter 1. Edge of Perimeter: "))
        self.b = int(input("Enter 2. Edge of Perimeter: "))
        self.c = int(input("Enter 3. Edge of Perimeter: "))
        self.perimeter()
        self.area()
        print("Triangle Area: " , self.result_A)
        print("Triangle Perimeter: " , self.result_P)


    def area(self):
        s = (self.a + self.b + self.c)/2
        self.result_A = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        return self.result_A

    def perimeter(self):

        self.result_P = self.a + self.b + self.c
        return self.result_P
        
class Rectangle:
    def __init__(self):
        self.a = int(input("Enter 1. Edge of Rectangle: "))
        self.b = int(input("Enter 2. Edge of Rectangle: "))
        self.area()
        self.perimeter()
        print("Rectangle Area: " , self.result_A)
        print("Rectangle Perimeter: " , self.result_P)
    
    def area(self):
        self.result_A = self.a * self.b
        return self.result_A
    
    def perimeter(self):
        self.result_P = 2*(self.a + self.b)
        return self.result_P
    
class Square(Rectangle):
    def __init__(self):
        self.a = int(input("Enter Edge of Square: "))
        self.b = self.a
        self.area()
        self.perimeter()
        print("Square Area: " , self.result_A)
        print("Square Perimeter: " , self.result_P)

class Cube(Square):
    def __init__(self):
        self.a = int(input("Enter Edge of Cube: "))
        self.surface_area()
        self.volume()
        print("Cube Surface Area: ", self.result_SA)
        print("Cube Volume: ",self.result_V)
    
    def surface_area(self):
        self.b = self.a
        self.result_SA = self.area() * 6
        return self.result_SA
    
    def volume(self):
        self.result_V = self.a **3
        return self.result_V

class Pyramid(Triangle,Square):
    def __init__(self):
        print('''
        1. Tetrahedron (floor is triangle)
        2. Square Pyramid (floor is square)
        ''')
        choise = input("Select your Pyramid: ")
        if choise == "1":
            self.t_pyramid()
        elif choise == "2":
            self.s_pyramid()
    
    def t_pyramid(self):

        self.a = int(input("Enter edge of Tetrahedron: "))
        self.b= self.a
        self.c = self.a
        self.result_TA = self.area() * 4
        self.result_TV = (2**0.5)*(self.a**3)/12
        print("Tetrahedron Surface Area: ", self.result_TA)
        print("Tetrahedron Volume: ",self.result_TV)
        
    def s_pyramid(self):
        self.a = int(input("Enter edge of Square: "))
        self.h = int(input("Enter height of Square Pyramid: "))
        result_TV = self.h * self.a**2
        result_TA = self.a * ((4*self.h**2 + self.a**2) + self.a)
        print("Square Pyramid Volume:", result_TV)
        print("squre Pyramid Area:",result_TA)       
def program():
    while True:
        print('''
        
        1. Triangle
        2. Rectangle
        3. Square
        4. Cube
        5. Pyramid
        6. Exit
        ''')
        choise = int(input("Select your shape: "))
        if choise == 1:
            Triangle()
        elif choise == 2:
            Rectangle()
        elif choise == 3:
            Square()
        elif choise == 4:
            Cube()
        elif choise == 5:
            Pyramid()
        elif choise == 6:
            break
        else:
            True

program()
### All Rights Reserved ###

#Copyright (c) ${shape(HM6).2021} ${Alper_Kaan}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.