#Write a Python program to list only directories, files and all directories, files in a specified path.
import os

path = input("Path:")

print("Directories in", path, ":")
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        print(item)
        
print("Files in", path, ":")
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(item)

print("Directories and files in", path, ":")
for item in os.listdir(path):
    print(item)