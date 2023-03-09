#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

file_path = input("Enter the file path to delete: ")

if os.path.exists(file_path):
    if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
      
        os.remove(file_path)
        print("File deleted successfully!")
    else:
        
        print("File exists but is not accessible.")
else:

    print("File does not exist.")
