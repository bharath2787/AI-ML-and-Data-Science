

'''
Polymorphism is in action because the same sound() method behaves differently based on the object calling it.
'''

class Animal:
    def sound(self):
        return "Animals make sounds"

class Dog(Animal):
    def sound(self):  # Overriding the sound() method
        return "Dog barks"

class Cat(Animal):
    def sound(self):  # Overriding the sound() method
        return "Cat meows"

# Usage
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.sound())

obj1 = Dog()
obj1.sound()
obj2 = Cat()
obj2.sound()
obj3 = Animal()
obj3.sound()
