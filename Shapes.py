import math                     # for pi
import sys                      # for sys.exit()
from abc import abstractmethod

class Shape (object):           # inherits from object
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
    def __init__ (self, l, w):
        self.__l = self.__w = 0             # private l,w being protected
        self.setLength(l)
        self.setWidth(w)
    
    def getName (self):
        return "Rectangle"

    def getArea (self):
        return self.__l * self.__w
    
    def __str__ (self):
        return "L = " + str(self.__l) + "; W = " + str(self.__w)

    def getLength (self):           # get/set l,w methods
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
    def __init__ (self, a):
        super().__init__(a, a)

    def getName (self):
        return "Square"
    
    def getSide(self):                      # get/set methods
        return super().getLength()
    def setSide(self, a):
        super().setLength(a)
        super().setWidth(a)


class Cube (Square):                        # inherits from Square
    def __init__ (self, a):
        super().__init__(a)

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

    def __isBlankList(self):
        return True if self.__getListSize() == 0 else False

    def __addShape (self, shape):
        self.__shapes.append(shape)

    def __removeShape (self, ndelete):
        self.__shapes.pop(ndelete)

    def __printShape (self, nprint):
        shape = self.__getList()[nprint]
        print("Shape", nprint+1, " ", shape.getName(), shape, "Area: ", shape.getArea(), " Volume: ", shape.getVolume())


    @staticmethod
    def __getChoiceInput (range):
        choice = 0
        gotChoiceCorrectly = False
        while gotChoiceCorrectly == False:
            try:
                choice = int(input("Please enter: "))
                if 0 < choice < range + 1:
                    gotChoiceCorrectly = True
                else:
                    print("You should enter your choice from 1 to", range, 
                    ", please try again: ")
            except(ValueError, SyntaxError):
                print("Your choice should be an integer, please try again: ")
        return choice

    @staticmethod
    def __checkxyInput():
        value = 0
        gotxyCorrectly = False
        while gotxyCorrectly == False:
            try:
                value = float(input())
                gotxyCorrectly = True
            except(ValueError, SyntaxError):
                print("The value of the coordinate should be a float, please try again: ", end = '')
        return value

    def __getxyInput(self):
        print("\nPlease enter the x-coordinates value", end = ': ')
        x = self.__checkxyInput()
        print("Please enter the y-coordinates value", end = ': ')
        y = self.__checkxyInput()
        return x, y

    @staticmethod
    def __getDimentionInput():
        value = 0
        gotDimentionCorrectly = False
        while gotDimentionCorrectly == False:
            try:
                value = float(input())
                if value > 0:
                    gotDimentionCorrectly = True
                else:
                    print("The value of its dimention should be positive, please try again: ")
            except(ValueError, SyntaxError):
                print("The value of its dimention should be a float, please try again: ")
        return value

    def __printSelectedShape (self):
        print("Please enter the number of the object you want to print: ")
        nselect = self.__getChoiceInput(self.__getListSize())
        self.__printShape(nselect-1)

    def __printWholeList (self):
        if self.__isBlankList():
            print("List is blank. You need to add an object first!") 
        else:
            for i in range(self.__getListSize()):
                self.__printShape(i)

    def __MenuOrExit (self):
        print("\nDo you want to return to the main menu?\n"
            + "1. Yes           2. Exit the program")
        choice = self.__getChoiceInput(2)
        if choice == 1:
            exit
        elif choice == 2:
            print("\nNice to meet you. Bye!")
            sys.exit()

    def __addShapeFromUser (self):
        print("\nChoose the shape you want to create and enter its number: \n" + 
            "1. Point \n" + "2. Circle\n" + "3. Cylinder \n" + "4. Sphere \n" +
            "5. Rectangle \n" + "6. Square \n" + "7. Cube")
        shapeNumber = self.__getChoiceInput(7)

        if shapeNumber == 1:
            x, y = self.__getxyInput()
            point = Point(x, y)
            self.__addShape(point)
        
        elif shapeNumber == 2:
            x, y = self.__getxyInput()
            print("Please enter the value of its radius", end = ': ')
            r = self.__getDimentionInput()
            circle = Circle(x, y, r)
            self.__addShape(circle)
            
        elif shapeNumber == 3:
            x, y = self.__getxyInput()
            print("Please enter the value of its radius", end = ': ')
            r = self.__getDimentionInput()
            print("Please enter the value of its height", end = ': ')
            h = self.__getDimentionInput()
            cylinder = Cylinder(x, y, r, h)
            self.__addShape(cylinder)

        elif shapeNumber == 4:
            x, y = self.__getxyInput()
            print("Please enter the value of its radius", end = ': ')
            r = self.__getDimentionInput()
            sphere = Sphere(x, y, r)
            self.__addShape(sphere)

        elif shapeNumber == 5:
            print("Please enter the value of its length", end = ': ')
            l = self.__getDimentionInput()
            print("Please enter the value of its width", end = ': ')
            w = self.__getDimentionInput()
            rectangle = Rectangle(l, w)
            self.__addShape(rectangle)

        elif shapeNumber == 6:
            print("Please enter the value of its side", end = ': ')
            a = self.__getDimentionInput()
            square = Square(a)
            self.__addShape(square)
        
        elif shapeNumber == 7:
            print("Please enter the value of its side", end = ': ')
            a = self.__getDimentionInput()
            cube = Cube(a)
            self.__addShape(cube)

        print("\nIt has been successfully added! New shape:")
        self.__printShape(self.__getListSize()-1)
        
        self.__MenuOrExit()

    def __removeShapeFromUser(self):
        if self.__isBlankList():
            print("\nThe list is blank, please add a shape first!")
        else:
            print("Enter the number of the shape you want to delete: ")
            ndelete = self.__getChoiceInput(self.__getListSize())
            self.__removeShape(ndelete - 1)
            print("The shape", ndelete, "has been successfully deleted!\n")
        self.__MenuOrExit()

    def __printListFromUser(self):
        if self.__isBlankList():
            print("The list is blank, please add a shape first!")
        else:
            print("\nDo you want to print a particular object, or print the whole list? \n" +
                    "1. Print a particular one \n" +
                    "2. Print the whole list")
            printchoice = self.__getChoiceInput(2)
            if printchoice == 1:
                self.__printSelectedShape()
            else:
                self.__printWholeList()
            
        self.__MenuOrExit()
    
    def __modifyShapeFromUser(self):
        if self.__isBlankList():
            print("\nList is blank. You need to add an object first!") 
        else:
            print("\nEnter the number of the shape you want to modify:")
            nmodify = self.__getChoiceInput(self.__getListSize()) - 1
            shape = self.__getList()[nmodify]
            shapename = shape.getName()
            
            print("\nThe details of the shape you selected are:")
            self.__printShape(nmodify)

            if shapename == "Point":
                print("\nWhich parameter you want to modify? \n"
                    + "1. x-axis \n"
                    + "2. y-axis")
                choice = self.__getChoiceInput(2)
                print("\nEnter the new value", end = " : ")
                value = self.__checkxyInput()
                if choice == 1:
                    self.__getList()[nmodify].setX(value)
                elif choice == 2:
                    self.__getList()[nmodify].setY(value)
                else:
                    print("Non expected error!")

            elif shapename == "Circle":
                print("\nWhich parameter you want to modify? \n"
                    + "1. x-axis \n"
                    + "2. y-axis \n"
                    + "3. radius ")
                choice = self.__getChoiceInput(3)
                print("\nEnter the new value", end = " : ")
                if choice == 1:
                    self.__getList()[nmodify].setX(self.__checkxyInput())
                elif choice == 2:
                    self.__getList()[nmodify].setX(self.__checkxyInput())
                elif choice == 3:
                    self.__getList()[nmodify].setRadius(self.__getDimentionInput())
                else:
                    print("Non expected error!")
            
            elif shapename == "Cylinder":
                print("\nWhich parameter you want to modify? \n"
                    + "1. x-axis \n"
                    + "2. y-axis \n"
                    + "3. radius \n"
                    + "4. height ")
                choice = self.__getChoiceInput(4)
                print("\nEnter the new value", end = " : ")
                if choice == 1:
                    self.__getList()[nmodify].setX(self.__checkxyInput())
                elif choice == 2:
                    self.__getList()[nmodify].setX(self.__checkxyInput())
                elif choice == 3:
                    self.__getList()[nmodify].setRadius(self.__getDimentionInput())
                elif choice == 4:
                    self.__getList()[nmodify].setHeight(self.__getDimentionInput())
                    
            elif shapename == "Sphere":
                print("\nWhich parameter you want to modify? \n"
                    + "1. x-axis \n"
                    + "2. y-axis \n"
                    + "3. radius ")
                choice = self.__getChoiceInput(3)
                print("\nEnter the new value", end = " : ")
                if choice == 1:
                    self.__getList()[nmodify].setX(self.__checkxyInput())
                elif choice == 2:
                    self.__getList()[nmodify].setX(self.__checkxyInput())
                elif choice == 3:
                    self.__getList()[nmodify].setRadius(self.__getDimentionInput())

            elif shapename == "Rectangle":
                print("\nWhich parameter you want to modify? \n"
                    + "1. length \n"
                    + "2. width ")
                choice = self.__getChoiceInput(2)
                print("\nEnter the new value", end = " : ")
                if choice == 1:
                    self.__getList()[nmodify].setLength(self.__getDimentionInput())
                elif choice == 2:
                    self.__getList()[nmodify].setWidth(self.__getDimentionInput())

            elif shapename == "Square":
                print("\nEnter the new value for its sides: ")
                self.__getList()[nmodify].setSide(self.__getDimentionInput())

            elif shapename == "Cube":
                print("\nEnter the new value for its sides", end = " : ")
                self.__getList()[nmodify].setSide(self.__getDimentionInput())
            
            else:
                print("Shape name not found! non expected error!")
            
            print("You have successfully modified this shape. \nNew shape details: ")
            self.__printShape(nmodify)
        
        self.__MenuOrExit()
                    

    def menu(self):
        print("\nPlease choose the function you want to use: \n"
            + "1. Add a new shape\n"
            + "2. Delete a shape \n"
            + "3. Modify a shape \n"
            + "4. Print out shapes \n"
            + "5. Exit the program")
        nmenu = self.__getChoiceInput(5)

        if nmenu == 1:
            self.__addShapeFromUser()
        elif nmenu == 2:
            self.__removeShapeFromUser()
        elif nmenu == 3:
            self.__modifyShapeFromUser()
        elif nmenu == 4:
            self.__printListFromUser()
        elif nmenu == 5:
            print("\nNice to meet you. Bye!")
            sys.exit(0)

# main
def main ():
    shapelist = ShapeList()
    while 1:
        shapelist.menu()


if __name__ == "__main__":
    main()

