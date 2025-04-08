# Provides high-level file operations,
# simplifying tasks that involve copying, moving, or archiving files and directories

import shutil
import os

def copy_file():
    # Copy a file from one location to another
    shutil.copy("source.txt", "destination.txt")  # Copies the file directly

    with open("source.txt", "r") as src:
        with open("destination.txt", "w") as dest:
            dest.write(src.read())

# shutil.move("source_file_or_folder", "destination_path_or_new_name")
# shutil.copytree("source_folder", "destination_folder")  # Recursively copy folder
# shutil.make_archive("example_archive", "zip", "source_directory") # Create a compressed archive (zip format)


