
'''
🦆 Duck Typing Demo for a Mathematics Problem in Python
In duck typing, Python doesn't check an object's type; instead, it checks if the object has the required method.
"If it walks like a duck and quacks like a duck, it must be a duck!"

🚀 Scenario:
We will create a function that performs addition on different types of objects (integers, floats, lists, tuples, NumPy arrays).

Instead of checking types explicitly, we assume that the object supports the + operator.
This is duck typing in action!


📝 Explanation:
1️⃣ Custom Classes (Number and ListNumbers)

These classes implement the __add__ method, allowing + operator usage.
Duck Typing lets us call perform_addition() without checking types.
2️⃣ Flexible perform_addition()

Works with integers, lists, tuples, NumPy arrays, and user-defined objects.
As long as an object supports +, Python executes it without complaints.


How does this work for different types?

If a is a ListNumbers object, it calls ListNumbers.__add__(), which performs element-wise addition.
If a is a tuple, Python calls the built-in tuple __add__(), which performs concatenation.
If a is a NumPy array, it calls numpy.ndarray.__add__(), which performs element-wise addition.
If a is a Number object, it calls Number.__add__(), which performs numeric addition.

'''



import numpy as np

class Number:
    """Represents a basic number."""
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value  # Enables + operator

class ListNumbers:
    """Represents a list of numbers."""
    def __init__(self, numbers):
        self.numbers = numbers

    def __add__(self, other):
        return [a + b for a, b in zip(self.numbers, other.numbers)]  # Element-wise addition

def perform_addition(a, b):
    """Performs addition without checking the type (Duck Typing)."""
    return a + b  # Works as long as + is supported!

# Using different data types
num1 = Number(10)
num2 = Number(20)
list1 = ListNumbers([1, 2, 3])
list2 = ListNumbers([4, 5, 6])
tuple1 = (10, 20, 30)
tuple2 = (1, 2, 3)
numpy_arr1 = np.array([10, 20, 30])
numpy_arr2 = np.array([5, 10, 15])

# Duck Typing in Action
print(perform_addition(num1, num2))       # Output: 30 (Number objects)
print(perform_addition(list1, list2))     # Output: [5, 7, 9] (Custom list addition)
print(perform_addition(tuple1, tuple2))   # Output: (10, 20, 30, 1, 2, 3) (Tuples concatenate)
print(perform_addition(numpy_arr1, numpy_arr2))  # Output: [15 30 45] (NumPy array element-wise addition)
