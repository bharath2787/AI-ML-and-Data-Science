import os  # Importing the os module to check file existence

def read_file_in_chunks(file_path, chunk_size=1024*1024):
    """
    Reads a file in chunks to handle large files efficiently.
    
    Arguments:
    file_path : str : The path to the file to be read
    chunk_size : int : The size of the chunk (in bytes), default is 1 MB
    """
    if os.path.exists(file_path):  # Check if the file exists
        with open(file_path, 'rb') as file:  # Open the file in binary read mode
            chunk = file.read(chunk_size)  # Read the first chunk
            while chunk:  # Continue reading until the end of the file
                print(chunk)  # Print or process the chunk (you can replace this with your own logic)
                chunk = file.read(chunk_size)  # Read the next chunk
    else:
        print(f'File {file_path} does not exist.')  # If the file does not exist, print a message

# Example usage
# replace 'example.txt' with your actual file path
read_file_in_chunks('example.txt')
