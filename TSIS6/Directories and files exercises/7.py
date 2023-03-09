#Write a Python program to copy the contents of a file to another file.
source_file = input("Copy Path: ")
destination_file = input("Write path: ")

with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
   
    destination.write(source.read())
