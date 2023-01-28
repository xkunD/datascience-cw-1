import random               # for Random class methods in a full version

class NumeberList:
    def __init__ (self):    # the class constructor
        self._data = []     # initialize the _data "private" instance variable to an empty list

    def getData (self):
        return self._data   # return the contained data list to users of the class

    def setData (self, data):
        self._data = data   # initialize the list with "externally-created" data
        

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
    mydata = [0.1, 1.1, 2.1, 3.1, 4.1]          # hardcoded data set values, list with 5 elements
    nlist = NumeberList()                       # create new empty NumberList object instance
    nlist.setData(mydata)                       # fill it in with the data set

    print("Numbers: " + str(nlist.getData()))               # print the data set
    print("Mean: " + str(mean(nlist.getData())))            # calculate and print mean
    print("Variance: " + str(variance(nlist.getData())))    # calculate and print variance

if __name__ == "__main__":
    main()