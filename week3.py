import numpy as np
class magicSquare:
    def __init__(self, size):
        self.size = 1
        self.setSize(size)
        self.square = np.random.random([self.size, self.size])
        self.square = self.square.round(0)

    def __str__(self):
        return "Square of " + str(self.size) + "\n" + str(self.square)

    def setSize(self, size):
        if(size>=1):
            self.size = size
    
    def isMagic(self):
        sum = 0
        for i in range(self.size):
            print("sum = ",sum, "square = ", self.square[i, i])
            sum = sum + self.square[i, i]
            
        if(self.square[:,0].sum()==sum and self.square[0,:].sum()==sum):
            return True
        else:
            return False

def main():
    s1 = magicSquare(-2)
    if(s1.isMagic()):
        print("This is a magic square")
    else:
        print("sorry not a magic number")

if __name__ == "__main__":
    main()