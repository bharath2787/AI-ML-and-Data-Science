
'''
Python allows overloading built-in operators (like +, -, *, etc.) 
using magic methods (also called dunder methods, e.g., __add__, __sub__, etc.).

✅ Example: Overloading the + Operator



✅ Without operator overloading, p1 + p2 would throw an error because + doesn’t work for custom objects. 
    But by defining __add__(), we make it work for Point objects.
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading the '+' operator
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):  # String representation
        return f"({self.x}, {self.y})"

# Usage
p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2  # Calls __add__
print(p3)  # Output: (6, 8)
