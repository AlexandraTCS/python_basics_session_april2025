import os
from os import path
import time

# Step 1: Define folder and file names
folder_name = "example_folder"
file_name = "example_file.txt"

# Step 2: Create the folder if it doesn't exist
if not path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created successfully!")
else:
    print(f"Folder '{folder_name}' already exists!")

# Step 3: Create and save the file inside the folder
file_path = path.join(folder_name, file_name)  # Generate the full path to the file

with open(file_path, "w") as file:
    file.write("This is a sample file created inside the folder.\n")
    file.write("You can add more content here!")
print(f"File '{file_name}' created and saved successfully at: {file_path}")

# Get the file size
file_size = path.getsize(file_path)
print(f"File Size: {file_size} bytes")

# Get the creation time of the file
creation_time = path.getctime(file_path)
print(f"File Creation Time (unformatted): {creation_time}")
#The output of  is a timestamp in the form of a floating-point number.
#This number represents the time in seconds since the epoch,
#which is typically January 1, 1970, 00:00:00 UTC (commonly referred to as Unix time).
print(f"File Creation Time: {time.ctime(creation_time)}")

# Get the modification time of the file
modification_time = os.path.getmtime(file_path)
print(f"File Last Modified Time: {time.ctime(modification_time)}")

# Get the absolute file path
absolute_path = path.abspath(file_path)
print(f"Absolute Path: {absolute_path}")
