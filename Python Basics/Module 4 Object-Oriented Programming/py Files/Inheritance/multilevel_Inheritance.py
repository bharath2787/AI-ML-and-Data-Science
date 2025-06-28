
'''
Multilevel Inheritance : A class inherits from another derived class, forming a chain.

✅ The Child class has access to both Parent and Grandparent methods.

'''

class Grandparent:
    def grandparent_method(self):
        return "Method from Grandparent"

class Parent(Grandparent):
    def parent_method(self):
        return "Method from Parent"

class Child(Parent):
    def child_method(self):
        return "Method from Child"

# Usage
obj = Child()
print(obj.grandparent_method())  # Output: Method from Grandparent
print(obj.parent_method())       # Output: Method from Parent
print(obj.child_method())        # Output: Method from Child
