import os  # Importing the os module to interact with the operating system

# Define the path to the file you want to create
file_path = "example.txt"

# Check if the file does not exist
if not os.path.exists(file_path):
    with open(file_path, 'w') as file:  # Open the file in write mode to create it
        print(f"{file_path} has been created.")  # Print confirmation after creating the file
else:
    print(f"{file_path} already exists.")  # If file exists, print a message
