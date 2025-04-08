#Purpose: Works exclusively with file content—reading, writing, appending, or creating files


# File Modes:https://www.geeksforgeeks.org/file-mode-in-python/

# Create or overwrite a file using 'w' mode
# 'w' (write mode): Opens a file for writing. If the file already exists, it will be overwritten.
# If the file does not exist, it will be created.
def create_file():
    file = open("example.txt", "w")  # Open the file for writing
    file.write("Second version\n")  # Write some text to the file
#    file.write("This file demonstrates file handling in Python.\n")
    file.close()  # Close the file to save changes


# Open and read the file using 'r' mode 
# 'r' (read mode): Opens a file for reading. Raises an error if the file doesn't exist.
def read_file():
    with open("example.txt", "r") as file:
#        content = file.read() 
        print("Reading file contents:\n")
        print(file.read())  # Read and display the content of the file
    
    
# Append to the file using 'a' mode 
# 'a' (append mode): Opens a file for writing, but does not overwrite existing content.
# Creates a new file if it does not exist.
def append_file():
    with open("example.txt", "a")  as file:
        file.write("This line was appended to the file.\n")  # Append new text        
        print("\nData appended successfully!")

def read_one_line():
    with open("example.txt", "r")  as file:
        print("Reading one line from the file:\n")
        print(file.readline())  # Read and display the first line of the file
        print(file.readline()) 

def line_loop():
    f = open("example.txt", "r")
    print("Reading line by line\n")
    for x in f:
        print(x)
    f.close()

#create_file()
#read_file()
#append_file()
#read_one_line()
#line_loop()