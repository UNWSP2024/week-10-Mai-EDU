# Programmer: Mai Lillie
# Date: 11/8/24
# Program # 2: Car Class

# Defines the class that has all the car functions
class Car:
    def __init__(self, year_model, make, speed):
        self.year_model = year_model
        self.make = make
        self.speed = speed
    def accelerate(self):
        self.speed += 5
    def brake(self):
        self.speed -= 5
    def get_speed(self):
        return self.speed

# Creates the car for this program
car1 = Car(2015, "Suv", 0)
# Speeds up the car, breaks it, and returns speed
for i in range(5):
    car1.accelerate()
    speed = car1.get_speed()
    print (speed)
car1.brake()
speed = car1.get_speed()
print (speed)
