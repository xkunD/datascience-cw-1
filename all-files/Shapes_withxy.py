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

class Rectangle (Point):                    # inherits from Point
    def __init__ (self, x, y, l, w):
        super().__init__(x, y)
        self.__l = self.__w = 0             # private l,w being protected
        self.setLength(l)
        self.setWidth(w)
    
    def getName (self):
        return "Rectangle"

    def getArea (self):
        return self.__l * self.__w
    
    def __str__ (self):
        return "C = " + super().__str__() + "; L = " + str(self.__l) + "; W = " + str(self.__w)

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
    def __init__ (self, x, y, a):
        super().__init__(x, y, a, a)

    def getName (self):
        return "Square"

    # inherits methods getArea and __str__ from Rectangle

    def getSide(self):                      # get/set a methods
        return super().getLength()
    def setSide(self, a):
        super().setLength(a)
        super().setWidth(a)


class Cube (Square):                        # inherits from Square
    def __init__ (self, x, y, a):
        super().__init__(x, y, a)

    def getName (self):
        return "Cube"

    def getArea (self):
        return 6.*super().getArea()

    def getVolume (self):
        return super().getArea() * self.getSide()

    def __str__ (self):
        return super().__str__() + "; H = " + str(self.getSide())


class ShapeList:
    def __init__ (self):
        self.__shapes = []

    def __getList (self):
        return self.__shapes

    def __getListSize (self):
        return len(self.__shapes)

    def __addShape (self, shape):
        self.__shapes.append(shape)

    def __removeShape (self, ndelete):
        self.__shapes.pop(ndelete - 1)
    
    def __isBlankList(self):
        if self.__getListSize() == 0:
            return True
        else:
            return False

    def __printShape (self, nprint):
        print("Shape", nprint+1, ": " + self.__getList()[nprint].getName() + " " + str(self.__getList()[nprint]) + " Area: " + str(self.__getList()[nprint].getArea()) + " Volume: " + str(self.__getList()[nprint].getVolume()))


    def __selectObjectFromKeyboard (self):
        nselect = 0
        gotNSelectCorrectly = False
        while gotNSelectCorrectly == False:
            try:
                nselect = int(input())
                if 0 < nselect <= self.__getListSize():
                    gotNSelectCorrectly = True
                else:
                    print("__selectObjectFromKeyboard: The number of selected object should be a positive integer within the list size!")
            except(ValueError, SyntaxError):
                print("__selectObjectFromKeyboard: The number of selected object should be an integer!")
        return nselect

    @staticmethod
    def __getShapeNumberFromKeyboard():
        print("Choose the shape you want to create and enter its number: \n" + 
            "1. Point \n" + "2. Circle\n" + "3. Cylinder \n" + "4. Sphere \n" +
            "5. Rectangle \n" + "6. Square \n" + "7. Cube")
        shapeNumber = 0
        gotShapeNumberCorrectly = False
        while gotShapeNumberCorrectly == False:
            try:
                shapeNumber = int(input())
                if 0 < shapeNumber < 8:
                    gotShapeNumberCorrectly = True
                else:
                    print("__getShapeNumberFromKeyboard: Shape number should be chosen from 1 to 7!")
            except(ValueError, SyntaxError):
                print("__getShapeNumberFromKeyboard: Shape number should be an integer!")
        return shapeNumber

    @staticmethod
    def __checkxyInput():
        value = 0
        gotxyCorrectly = False
        # maybe we dont need the while loop because no if else?
        while gotxyCorrectly == False:
            try:
                value = float(input())
                gotxyCorrectly = True
            except(ValueError, SyntaxError):
                print("__checkxyInput: The value of the coordinate should be a float!")
        return value

    @staticmethod
    def __checkDimentionInput():
        value = 0
        gotDimentionCorrectly = False
        while gotDimentionCorrectly == False:
            try:
                value = float(input())
                if value > 0:
                    gotDimentionCorrectly = True
                else:
                    print("__checkDimentionInput: The value of its dimention must be positive!")
            except(ValueError, SyntaxError):
                print("__checkDimentionInput: The value of its dimention should be a float!")
        return value

    def __getXFromKeyboard(self):
        print("Please enter the x-coordinates value: ")
        x = self.__checkxyInput()
        return x

    def __getYFromKeyboard(self):
        print("Please enter the y-coordinates value: ")
        y = self.__checkxyInput()
        return y


    @staticmethod
    def __getPrintChoiceFromKeyboard():
        printchoice = 0
        gotPrintChoiceCorrectly = False
        while gotPrintChoiceCorrectly == False:
            try:
                printchoice = int(input())
                if printchoice == 1 or printchoice == 2:
                    gotPrintChoiceCorrectly = True
                else:
                    print("printList: The choice number should be either 1 or 2!")
            except(ValueError, SyntaxError):
                print("printList: The choice number should be an integer!")
        return printchoice

    def __printSelectedObject (self):
        print("Please enter the number of the object you want to print: ")
        nselect = self.__selectObjectFromKeyboard()
        self.__printShape(nselect-1)

    def __printWholeList (self):
        if self.__isBlankList():
            print("List is blank. You need to add an object first!") 
        else:
            for i in range(self.__getListSize()):
                self.__printShape(i)

    def __addShapeFromKeyboard (self):
        shapeNumber = self.__getShapeNumberFromKeyboard()
        x = self.__getXFromKeyboard()
        y = self.__getYFromKeyboard()
        
        # add a while loop for getting it right?

        if shapeNumber == 1:
            point = Point(x, y)
            self.__addShape(point)
        
        elif shapeNumber == 2:
            print("Please enter the value of its radius: ")
            r = self.__checkDimentionInput()
            circle = Circle(x, y, r)
            self.__addShape(circle)
            
        elif shapeNumber == 3:
            print("Please enter the value of its radius: ")
            r = self.__checkDimentionInput()
            print("Please enter the value of its height: ")
            h = self.__checkDimentionInput()
            cylinder = Cylinder(x, y, r, h)
            self.__addShape(cylinder)

        elif shapeNumber == 4:
            print("Please enter the value of its radius: ")
            r = self.__checkDimentionInput()
            sphere = Sphere(x, y, r)
            self.__addShape(sphere)

        elif shapeNumber == 5:
            print("Please enter the value of its length: ")
            l = self.__checkDimentionInput()
            print("Please enter the value of its width: ")
            w = self.__checkDimentionInput()
            rectangle = Rectangle(x, y, l, w)
            self.__addShape(rectangle)

        elif shapeNumber == 6:
            print("Please enter the value of its side: ")
            a = self.__checkDimentionInput()
            square = Square(x, y, a)
            self.__addShape(square)
        
        elif shapeNumber == 7:
            print("Please enter the value of its side: ")
            a = self.__checkDimentionInput()
            cube = Cube(x, y, a)
            self.__addShape(cube)

        print("The new shape with number", self.__getListSize(), "has been successfully added!")

    def __removeShapeFromKeyboard(self):
        if self.__isBlankList():
            print("The list is blank, please add a shape first!")
        else:
            print("Enter the number of the shape you want to delete: ")
            ndelete = self.__selectObjectFromKeyboard()
            self.__removeShape(ndelete)
            print("The shape", ndelete, "has been successfully deleted!\n")

    def __printList(self):
        print("Do you want to print a particular object, or print the whole list? \n" +
                "1. Print a particular one \n" +
                "2. Print the whole list")
        printchoice = self.__getPrintChoiceFromKeyboard()
        if printchoice == 1:
            self.__printSelectedObject()
        else:
            self.__printWholeList()
    
    def __modifyShape(self):
        print("Enter the number of the shape you want to modify:")
        

    def menu(self):
        print("\nPlease choose the function you want to use and enter its number: \n"
            + "1. Add a new shape\n"
            + "2. Print out \n"
            + "3. Delete a shape \n"
            + "4. Modify a shape \n"
            + "5. Exit the program")
        nmenu = 0

        try:
            nmenu = int(input())
            if nmenu == 1:
                self.__addShapeFromKeyboard()
            elif nmenu == 2:
                self.__printList()
            elif nmenu == 3:
                self.__removeShapeFromKeyboard()
            elif nmenu == 4:
                print("not yet implemented!")
            elif nmenu == 5:
                exit
            else:
                print("You should choose from choice 1 to 4!")
        except(ValueError, SyntaxError):
            print("The choice should be entered as a number!")

# main
def main ():
    shapelist = ShapeList()
    while 1:
        shapelist.menu()


if __name__ == "__main__":
    main()




