import random               # for Random class methods in a full version

class NumberList:
    def __init__ (self):    # the class constructor
        self.__data = []    # initialize the _data "private" instance variable to an empty list

    def getData (self):
        return self.__data  # return the contained data list to users of the class

    def setData (self, data):
        self.__data = data  # initialize the list with "externally-created" data

    @staticmethod
    def __getNDataFromKeyboard():       # private method
        print("Enter the number of data set elements: ")
        ndata = 0
        gotNDataCorrectly = False       # a flag to loop until we get ndata correctly
        while gotNDataCorrectly == False:
            try:
                ndata = float(input())
                if ndata % 1 == 0 and ndata >= 2:
                    gotNDataCorrectly = True
                else:
                    print("__getNDataFromKeyboard: ndata should be >=2")
            except (ValueError, SyntaxError):
                print("__getNDataFromKeyboard: ndata should be an integer!")
        # end while loop
        return int(ndata)               # return ndata as int
    
    def getDataFromKeyboard (self):
        ndata = self.__getNDataFromKeyboard()
        gotDataCorrectly = False
        while gotDataCorrectly == False:
            try:
                input_list = input("Enter the data set with spaces:").split()
                if(len(input_list) == ndata):
                    for i in range(ndata):
                        self.__data.append(float(input_list[i]))
                    gotDataCorrectly = True
                elif(len(input_list) > ndata or len(input_list) < ndata):
                    print("getDataFromKeyboard: the number of input dataset elements must be same as ndata.")
            except (ValueError, SyntaxError):
                print("getDataFromKeyboard: data should be a list of float!")

    def getRandomData (self, ndata, range1, range2=0):
        try:
            if (int(range2) == 0):
                low = 0;
                high = int(range1)
                number = int(ndata)
            else:
                low = int(range1)
                high = int(range2)
                number = int(ndata)
        except(ValueError, SyntaxError):
            print("ndata, range1, range2 should be integers or stringfied integers!" )
        for i in range (number):
            self.__data.append(random.randrange(low, high))

    def getDataFromFile (self, fileName):  
        file = open(fileName, 'r')
        try:
            for line in file:
                self.__data.append(float(line.strip('\n')))
        except(ValueError, SyntaxError):
            print("The file can not be converted to float list!" )
        
# end class

def mean(data):
    sum_value = sum(data)
    return sum_value/len(data)

def variance(data):
    n = len(data)
    sum_value = sum(data)
    mean_value = sum_value/n
    sum_sqr = 0
    for i in range(n):
        sum_sqr = sum_sqr + (data[i] - mean_value)**2
        # print("the difference is " , (data[i] - mean_value))
    var = sum_sqr / (n-1)
    return var

def main():
   
    # mydata = [0.1, 1.1, 2.1, 3.1, 4.1]          # hardcoded data set values, list with 5 elements
    nlist = NumberList()                       # create new empty NumberList object instance
    # nlist.setData(mydata)                       # fill it in with the data set
    
    # nlist.getDataFromKeyboard()

    # nlist.getRandomData2(5, 10)

    nlist.getDataFromFile("dataFile")

    print("Numbers: " + str(nlist.getData()))               # print the data set
    print("Mean: " + str(mean(nlist.getData())))            # calculate and print mean
    print("Variance: " + str(variance(nlist.getData())))    # calculate and print variance

    # print(nlist._NumberList__getNDataFromKeyboard())

if __name__ == "__main__":
    main()



# problem: value error exception not used in keyboard