import os  # Importing the os module to interact with the operating system

# Define the path to the file where you want to write
file_path = "example.txt"

# Open the file in write mode ('w'), which will create the file if it doesn't exist
with open(file_path, 'w') as file:
    file.write("This is a new line written to the file.\n")  # Write a line of text to the file
    print(f"Data has been written to {file_path}.")  # Print confirmation after writing
