# The program to write should emulate virtual dice throwing. It should get from the keyboard the number of sides of the virtual dice and the number of times to be thrown, the latter should be a multiple of the number of sides. The program should then throw the dice and print out the number of times each side occurred. Given that random numbers will be used, you should be able to see that the higher the number of throws, the closer the results will be towards approximately equal occurrence of all sides (same probability). The program should deal gracefully with incorrect type of arguments through checks and exceptions.

import sys
import random

def main():
    
    nsides = nthrows = 0

    # check nsides
    print("Please enter the number of sides of the dice:")
    try:
        nsides = int(input())
    except(ValueError, SyntaxError):
        print("nsides should be a number, program exiting!")
        sys.exit

    # check nthrows (integer & the multiple of nsides)
    print("Please enter the number of throws:")
    try:
        nthrows = int(input())
    except(ValueError, SyntaxError):
        print("nthrows should be a number, program exiting!")
        sys.exit

    if nthrows < nsides or nthrows % nsides != 0:
        print("nthrows should be >= nsides and also multiple of nsides, program exiting!")
        sys.exit
    
    facestimes = [0]*nsides                 # initialize facetimes
    
    random.seed(100)

    # loop to throw the dices
    for i in range (nthrows):               
        value = random.randrange(0, nsides)
        # print(value)
        facestimes[value] += 1

    for n in range (nsides):
        print("Side {} came {} times".format(n+1, facestimes[n]))


if __name__ == "__main__":
    main()

