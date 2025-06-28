'''

Explanation:

Vehicle is an abstract class.
start_engine() is an abstract method that must be implemented by subclasses.
Car and Bike provide implementations for start_engine().
Instantiating Vehicle directly would result in an error

We use the ABC module (abc stands for Abstract Base Class) to define abstract classes and methods.


'''




from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        """Abstract method that must be implemented in a subclass"""
        pass

# Concrete class implementing the abstract method
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

# Creating instances
car = Car()
car.start_engine()  # Output: Car engine started

bike = Bike()
bike.start_engine()  # Output: Bike engine started
