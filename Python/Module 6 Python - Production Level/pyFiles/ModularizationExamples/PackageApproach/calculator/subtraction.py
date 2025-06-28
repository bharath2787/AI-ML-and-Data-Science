"""
This module provides the subtraction operation for the calculator package.

Functions:
    subtract(a, b): Returns the difference between a and b.
"""

def subtract(a, b):
    """
    Subtracts the second number from the first.

    Parameters:
    a (int, float): The number to subtract from.
    b (int, float): The number to subtract.

    Returns:
    int, float: The difference between a and b.
    """
    return a - b

if __name__ == "__main__":
    """
    Executes a test case for the subtract function when run directly as a script.
    """
    a, b = 10, 5
    print(f"Subtraction: {subtract(a, b)}")  # Output: 5
