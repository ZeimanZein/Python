#Write a Python program to copy the contents of a file to another file.

source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")


with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
    
    destination.write(source.read())
    
print("File copied successfully!")
