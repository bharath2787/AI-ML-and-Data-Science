'''
Hierarchical Inheritance : Multiple child classes inherit from the same parent class.

✅ Both Child1 and Child2 inherit from Parent, but they can also define their own methods.

'''




class Parent:
    def show(self):
        return "Method from Parent"

class Child1(Parent):
    def child1_method(self):
        return "Method from Child1"

class Child2(Parent):
    def child2_method(self):
        return "Method from Child2"

# Usage
obj1 = Child1()
print(obj1.show())  # Output: Method from Parent

obj2 = Child2()
print(obj2.show())  # Output: Method from Parent
