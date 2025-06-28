"""
This module provides the multiplication operation for the calculator package.

Functions:
    multiply(a, b): Returns the product of a and b.
"""

def multiply(a, b):
    """
    Multiplies two numbers.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The product of a and b.
    """
    return a * b

if __name__ == "__main__":
    """
    Executes a test case for the multiply function when run directly as a script.
    """
    a, b = 10, 5
    print(f"Multiplication: {multiply(a, b)}")  # Output: 50
