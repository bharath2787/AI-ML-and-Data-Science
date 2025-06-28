"""
This module provides the addition operation for the calculator package.

Functions:
    add(a, b): Returns the sum of a and b.
"""

def add(a, b):
    """
    Adds two numbers.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The sum of a and b.
    """
    return a + b

if __name__ == "__main__":
    """
    Executes a test case for the add function when run directly as a script.
    """
    a, b = 10, 5
    print(f"Addition: {add(a, b)}")  # Output: 15
    print("this message will be printed whenever we run this py as script")
