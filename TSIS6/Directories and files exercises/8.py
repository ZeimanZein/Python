#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

file_path = input("Path to delete: ")

if os.path.exists(file_path):
    if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("Deleted successfully")
    else:
        print("Not accessible.")
else:
    print("File does not exist.")
