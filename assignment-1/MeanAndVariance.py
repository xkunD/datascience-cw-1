from NumberList import NumberList       # NumberList class is in file NumberList.py
import sys                              # for sys.argv and sys.exit()

def mean(data):
    sum_value = sum(data)
    return sum_value/len(data)

def variance(data):
    n = len(data)
    mean_value = mean(data)
    sum_sqr = 0
    for i in range(n):
        sum_sqr = sum_sqr + (data[i] - mean_value)**2
    var = sum_sqr / (n-1)
    return var

def main ():
    nlist = NumberList()        # create an empty NumberList instance

    nargs = len(sys.argv)       # argv contains the program name and arguments, as in C
    if nargs == 1:              # no arguments, actually only the program name hence value 1
        nlist.getDataFromKeyboard()
    elif nargs == 2:
        nlist.getDataFromFile(sys.argv[1])
    elif nargs == 3 or nargs == 4:
        if nargs == 3:
            nlist.getRandomData(sys.argv[1], sys.argv[2])
        else:                   # nargs = 4
            nlist.getRandomData(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("incorrect number of arguments, try again");
        sys.exit()              # terminate program

    print("Numbers: " + str(nlist.getData())) 
    print("Mean: " + str(mean(nlist.getData()))) 
    print("Variance: " + str(variance(nlist.getData())))

if __name__ == "__main__":
    main()

