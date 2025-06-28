import os  # Importing the os module to interact with the operating system

# Define the path to the file where you want to append data
file_path = "example.txt"

# Open the file in append mode ('a'), which will not overwrite the existing content
with open(file_path, 'a') as file:
    file.write("This is a new line appended to the file.\n")  # Append a line of text to the file
    print(f"Data has been appended to {file_path}.")  # Print confirmation after appending
