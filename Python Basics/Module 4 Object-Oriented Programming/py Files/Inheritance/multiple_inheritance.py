'''Multiple Inheritance
A child class inherits from more than one parent class.

✅ The Child class inherits methods from both Parent1 and Parent2.

🔹 Note: If both parents have a method with the same name, 
          Python follows the Method Resolution Order (MRO) to decide which method to call first.

'''


class Parent1:
    def method1(self):
        return "Method from Parent1"

class Parent2:
    def method2(self):
        return "Method from Parent2"

class Child(Parent1, Parent2):  # Inheriting from multiple parents
    pass

# Usage
obj = Child()
print(obj.method1())  # Output: Method from Parent1
print(obj.method2())  # Output: Method from Parent2


