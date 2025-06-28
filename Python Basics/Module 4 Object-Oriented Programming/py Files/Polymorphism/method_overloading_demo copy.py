
'''

Here's a Python class that demonstrates method overloading using both default parameters and variable-length arguments (*args) for mathematical operations.

Features of This Code:
✅ Uses default parameters to handle optional arguments.
✅ Uses *args (variable-length arguments) to support multiple numbers.
✅ Implements basic math operations: addition, multiplication, and finding the maximum number.


💡 Key Learnings
🔹 Default parameters allow flexible method signatures.
🔹 Variable-length arguments (*args) enable handling any number of inputs dynamically.
🔹 Python does not support traditional method overloading, but these techniques simulate it effectively.
'''


class MathOperations:
    def add(self, a, b, c=0):
        """Addition with method overloading using default parameter."""
        return a + b + c  # If `c` is not provided, defaults to 0
    def printhello(hellomessage):
        print(f"this is the hello message {hellomessage}")
    def multiply(self, *args):
        """Multiplication with method overloading using variable-length arguments."""
        result = 1
        for num in args:
            result *= num  # Multiply all numbers in `args`
        return result
    
    def max_value(self, *args):
        """Find maximum number using variable-length arguments."""
        if args:
            return max(args)
        return "No numbers provided"

# Usage
math_obj = MathOperations()
obj2 = MathOperations()

# # Addition
# print(math_obj.add(10, 20))        # Output: 30
# print(math_obj.add(10, 20, 30))    # Output: 60

# # Multiplication
# print(math_obj.multiply(2, 3))           # Output: 6
# print(math_obj.multiply(2, 3, 4, 5))     # Output: 120
# print(math_obj.multiply(7))              # Output: 7

# # Maximum Value
# print(math_obj.max_value(5, 10, 15, 2))  # Output: 15
# print(math_obj.max_value())              # Output: No numbers provided


print(f"this is a test {obj2.printhello("welcome")}") 

# printhello(obj2, "welcome")