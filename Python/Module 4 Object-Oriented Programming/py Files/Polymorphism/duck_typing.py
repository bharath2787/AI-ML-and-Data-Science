
'''
✅ The function make_sound() doesn’t care if the object is a Dog or Cat—it just calls sound().
 This is pure polymorphism in Python.

'''

class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

def make_sound(animal):  # Works with any object that has a `sound()` method
    return animal.sound()

# Usage
dog = Dog()
cat = Cat()

print(make_sound(dog))  # Output: Woof!
print(make_sound(cat))  # Output: Meow!
