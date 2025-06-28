'''
Single Inheritance
A child class inherits from a single parent class.
'''
class Parent:
    def show(self):
        return "I am a parent class method"

class Child(Parent):  # Inheriting from Parent
    pass

# Usage
obj = Child()
print(obj.show())  # Output: I am a parent class method
