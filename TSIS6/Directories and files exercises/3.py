#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

path = input("Path:")

if os.path.exists(path):
    print("Path exists!")
    
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")
else:
    print("Path does not exist.")
   