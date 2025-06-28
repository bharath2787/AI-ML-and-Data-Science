import os  # Importing the os module to interact with the operating system

# Define the path to the file you want to check
file_path = "example.txt"

# Check if the file exists using os.path.exists()
if os.path.exists(file_path):
    print(f"{file_path} exists.")  # If file exists, print a message
else:
    print(f"{file_path} does not exist.")  # If file does not exist, print a message
