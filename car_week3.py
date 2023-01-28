class Car:
    def __init__(self, make, model, engSize): # the constructor
        self.make = make 
        self.model = model 
        self.engSize = engSize

    def __str__(self):
        return "Car: " + str(self.make) + " " + str(self.model) + " " + str(self.engSize)


def main():
    cars = []
    car1 = Car("VW", "Golf GTI", 2000)
    car2 = Car("Porsche", "Boxter S", 3400)
    cars.append(car1)
    cars.append(car2)
    for c in cars:
        print(str(c))

    
if __name__ == "__main__":
    main()
