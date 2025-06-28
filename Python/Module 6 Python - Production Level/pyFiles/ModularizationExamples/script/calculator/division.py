print(f"name is :{__name__}")
def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

if __name__ == "__main__":
    a, b = 10, 5
    print(f"Division: {divide(a, b)}")  # Output: 2.0
