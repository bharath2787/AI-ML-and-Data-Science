
'''
Hybrid Inheritance : A combination of multiple types of inheritance.

✅ Hybrid inheritance combines different types, and Python uses MRO to determine the method resolution.

'''




class A:
    def method_a(self):
        return "Method from A"

class B(A):
    def method_b(self):
        return "Method from B"

class C(A):
    def method_c(self):
        return "Method from C"

class D(B, C):  # Inheriting from both B and C
    def method_d(self):
        return "Method from D"

# Usage
obj = D()
print(obj.method_a())  # Output: Method from A
print(obj.method_b())  # Output: Method from B
print(obj.method_c())  # Output: Method from C
print(obj.method_d())  # Output: Method from D
