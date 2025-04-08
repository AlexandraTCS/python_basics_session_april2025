import os

#The OS is module that provides a way to interact with the operating system.
#Interacting with file system structures, such as creating directories or handling paths.
#https://www.w3schools.com/python/module_os.asp


# Get the current working directory
current_dir = os.getcwd()
print(f"Current Working Directory: {current_dir}")

# List all files and directories in the current working directory
items = os.listdir()
print("Files and Folders in Current Directory:")
for item in items:
    print(item)

# Check if a file or directory exists
path = "example.txt"
if os.path.exists(path):
    print(f"'{path}' exists!")
else:
    print(f"'{path}' does not exist!")


# Remove a file
file_to_remove = "example.txt"
try:
    os.remove(file_to_remove)
    print(f"File '{file_to_remove}' removed successfully!")
except FileNotFoundError:
    print(f"Error: File '{file_to_remove}' not found!")
