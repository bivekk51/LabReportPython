class Vehicle:
    def start(self):
        print("The vehicle is starting")
class Car (Vehicle):
    def start(self):
        print("The car is starting")
class Bike(Vehicle):
    def start(self):
        print("The bike is starting")
vehicle1=Vehicle()
car1=Car()
bike1=Bike()

vehicle1.start()
car1.start()
bike1.start()