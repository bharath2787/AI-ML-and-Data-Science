import os  # Importing the os module to interact with the operating system

# Define the path to the file you want to delete
file_path = "example.txt"

# Check if the file exists before attempting to delete it
if os.path.exists(file_path):
    os.remove(file_path)  # Delete the file using os.remove()
    print(f"{file_path} has been deleted.")  # Print confirmation after deleting the file
else:
    print(f"{file_path} does not exist, so it cannot be deleted.")  # If file does not exist, print a message
