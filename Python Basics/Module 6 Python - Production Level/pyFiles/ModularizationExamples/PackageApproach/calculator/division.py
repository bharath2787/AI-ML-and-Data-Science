"""
This module provides the division operation for the calculator package.

Functions:
    divide(a, b): Returns the quotient of a divided by b. If b is zero, it returns an error message.
"""

def divide(a, b):
    """
    Divides the first number by the second.

    Parameters:
    a (int, float): The numerator.
    b (int, float): The denominator.

    Returns:
    int, float, str: The quotient of a and b, or an error message if b is zero.
    """
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

if __name__ == "__main__":
    """
    Executes a test case for the divide function when run directly as a script.
    """
    a, b = 10, 5
    print(f"Division: {divide(a, b)}")  # Output: 2.0
