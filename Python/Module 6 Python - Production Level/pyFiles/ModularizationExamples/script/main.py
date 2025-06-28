from calculator import add, subtract, multiply, divide



# If we remove __init__.py, then in main.py we would have to import each module manually:

# from calculator.addition import add
# from calculator.subtraction import subtract
# from calculator.multiplication import multiply
# from calculator.division import divide

# This is more verbose and harder to maintain.


print("Folder-Level Modularization Example")

a, b = 10, 5

# print(f"Addition: {add(a, b)}")       # Output: 15
# print(f"Subtraction: {subtract(a, b)}")  # Output: 5
# print(f"Multiplication: {multiply(a, b)}")  # Output: 50
print(f"Division: {divide(a, b)}")     # Output: 2.0
