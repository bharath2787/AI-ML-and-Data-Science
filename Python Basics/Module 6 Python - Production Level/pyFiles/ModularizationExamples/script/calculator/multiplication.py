print(f"name is :{__name__}")

def multiply(a, b):
    return a * b

if __name__ == "__main__":  # if the file is directly being run as script
    a, b = 10, 5
    print(f"Multiplication: {multiply(a, b)}")  # Output: 50
