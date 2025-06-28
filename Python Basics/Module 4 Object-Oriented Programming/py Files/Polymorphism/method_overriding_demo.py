'''
Method Overriding Demo for a Mathematics Problem
In this example, we'll use method overriding to create a base class MathOperations and override its methods in a child class AdvancedMath to modify the behavior.

🚀 Scenario:
Parent Class (MathOperations): Provides basic math operations (add(), multiply()).
Child Class (AdvancedMath):
Overrides add() to support multiple numbers.
Overrides multiply() to return 1 if no arguments are provided.

📝 Explanation:
1️⃣ Method Overriding in add():

The parent class only supports two numbers.
The child class overrides it to support any number of numbers using *args.
2️⃣ Method Overriding in multiply():

The parent class only supports two numbers.
The child class overrides it to support any number of numbers.
It also ensures multiplication returns 1 if no input is provided (mathematical identity property).


🔹 Key Takeaways
✅ Method overriding allows modifying or extending behavior in child classes.
✅ Base class remains simple, while child class adds flexibility.
✅ Dynamic argument handling (*args) makes methods more versatile.
'''


class MathOperations:
    """Base class with basic math operations."""
    def add(self, a, b):
        """Adds two numbers."""
        return a + b
    
    def multiply(self, a, b):
        """Multiplies two numbers."""
        return a * b

class AdvancedMath(MathOperations):
    """Child class overriding methods to enhance functionality."""
    def add(self, *args):
        """Adds multiple numbers (overridden method)."""
        return sum(args)  # Overriding to support multiple numbers

    def multiply(self, *args):
        """Multiplies multiple numbers, returns 1 if no input."""
        if not args:
            return 1  # Default multiplication value
        result = 1
        for num in args:
            result *= num
        return result

# Usage
basic_math = MathOperations()
advanced_math = AdvancedMath()

# Parent class behavior
print("Basic Math:")
print(basic_math.add(10, 20))       # Output: 30
print(basic_math.multiply(5, 4))    # Output: 20

# Child class (overridden methods)
print("\nAdvanced Math:")
print(advanced_math.add(10, 20, 30, 40))   # Output: 100 (supports multiple numbers)
print(advanced_math.multiply(2, 3, 4))     # Output: 24 (supports multiple numbers)
print(advanced_math.multiply())            # Output: 1 (default value if no input)





