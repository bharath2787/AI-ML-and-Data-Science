import os  # Importing the os module to interact with the operating system

# Define the path to the file you want to read from
file_path = "example.txt"

# Check if the file exists before attempting to read it
if os.path.exists(file_path):
    with open(file_path, 'r') as file:  # Open the file in read mode ('r')
        content = file.read()  # Read the content of the file
        print(f"Content of {file_path}:\n{content}")  # Print the content of the file
else:
    print(f"{file_path} does not exist.")  # If file does not exist, print a message
