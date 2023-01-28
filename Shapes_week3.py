import math                     # for pi
from abc import abstractmethod

class Shape (object):           # inherits from object
    # the following methods constitute a shape’s “interface” 
    # and should be redefined in all derived classes

    @abstractmethod
    def getName (self):
        pass                    # could also put return but this “implies” implementation

    @abstractmethod
    def getArea (self):
        pass

    @abstractmethod
    def getVolume (self):
        pass

class Point (Shape):            # inherits from abstract class Shape
    def __init__ (self, x, y):
        self.__x = x            # we make x, y private in order to align with
        self.__y = y            # Circle/Cylinder in which r, h have to be private

    def getName (self):
        return "Point"

    def __str__ (self):
        return "[" + str(self.__x) + "," + str(self.__y) + "]"
    
    # get/set x, y methods
    def getX (self):
        return self.__x
    def getY (self):
        return self.__y
    def setX (self, x):
        self.__x = x
    def setY (self, y):
        self.__y = y


class Circle (Point):               # inherits from Point
    def __init__ (self, x, y, r):
        super().__init__(x, y)      # red throughout means ‘reuse’
        self.__r = 0                # setRadius sets it only if r>0
        self.setRadius(r) 

    def getName (self):
        return "Circle"
    
    def getArea (self):
        return math.pi*self.__r*self.__r
    
    def __str__ (self):
        return "C = " + super().__str__() + "; R = " + str(self.__r)

    def getRadius (self):               # get/set radius methods, set protects r
        return self.__r
    def setRadius (self, r):
        if r > 0:
            self.__r = r

class Cylinder (Circle):                # inherits from Circle
    def __init__ (self, x, y, r, h):
        super().__init__(x, y, r)       
        self.__h = 0                    # setHeight initializes it only if h>0
        self.setHeight(h)

    def getName (self):
        return "Cylinder"

    def getArea (self):
        return 2.*super().getArea() + 2.*math.pi*self.getRadius()*self.__h

    def getVolume (self):
        return super().getArea()*self.__h

    def __str__ (self):
        return super().__str__() + "; H = " + str(self.__h)

    def getHeight (self):               # get/set height methods, set protects h
        return self.__h
    def setHeight (self, h):
        if h > 0:
            self.__h = h

class Sphere (Circle):                # inherits from Circle
    def __init__ (self, x, y, r):
        super().__init__(x, y, r)       # red throughout means ‘reuse’

    def getName (self):
        return "Sphere"

    def getArea (self):
        return 4.*super().getArea()

    def getVolume (self):
        return 4./3 * self.getRadius() * self.getRadius() * self.getRadius()

    def __str__ (self):
        return super().__str__()

class Rectangle (Shape):                    # Doing in composition from Shape
    def __init__ (self, x1, y1, x2, y2, l, w):
        self.__point1 = Point(x1, y1)
        self.__point2 = Point(x2, y2)
        self.__l = self.__w = 0             # private l,w being protected
        self.setLength(l)
        self.setWidth(w)
    
    def getName (self):
        return "Rectangle"

    def getArea (self):
        return self.__l * self.__w
    
    def __str__ (self):
        return "P1 = " + self.__point1.__str__() + ", P2 = " + self.__point2.__str__() + "; L = " + str(self.__l) + "; W = " + str(self.__w)

    # get/set l,w methods
    def getLength (self):
        return self.__l   
    def getWidth (self):
        return self.__w
    def setLength (self, l):
        if l > 0:
            self.__l = l
    def setWidth (self, w):
        if w > 0:
            self.__w = w


class Square (Rectangle):                   # inherits from Rectangle
    def __init__ (self, x1, y1, x2, y2, a):
        super().__init__(x1, y1, x2, y2, a, a)

    def getName (self):
        return "Square"
    
    def getSide(self):                      # get/set methods
        return super().getLength()
    def setSide(self, a):
        super().setLength(a)
        super().setWidth(a)


class Cube (Square):                        # inherits from Square
    def __init__ (self, x1, y1, x2, y2, a):
        super().__init__(x1, y1, x2, y2, a)

    def getName (self):
        return "Cube"

    def getArea (self):
        return 6.*super().getArea()

    def getVolume (self):
        return super().getArea() * self.getSide()

    def __str__ (self):
        return super().__str__() + "; H = " + str(self.getSide())



# main
def main ():
    point = Point(10, 20)
    circle = Circle(30, 40, 5)
    cylinder = Cylinder(50, 60, 10, 20)
    sphere = Sphere(10, 10, 5)
    rectangle = Rectangle(10, 11, 11, 10, 3, 5)
    square = Square(10, 10, 11, 11, 5)
    cube = Cube(10, 10, 5, 5, 2)

    shapes = []
    shapes.append(point) 
    shapes.append(circle) 
    shapes.append(cylinder)
    shapes.append(sphere)
    shapes.append(rectangle)
    shapes.append(square)
    shapes.append(cube)

    # we treat all the objects in list shapes polymorphically, by calling the Shape class methods getName, getArea and getVolume
    for s in shapes:
        print(s.getName() + " " + str(s) + " Area: " + str(s.getArea()) + " Volume: " + str(s.getVolume()))


if __name__ == "__main__":
    main()