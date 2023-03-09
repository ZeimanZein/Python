#Write a Python program to count the number of lines in a text file.
filename = input("Enter the file path: ")

with open(filename, 'r') as file:
   
    num_lines = 0
    for line in file:
        num_lines += 1

print(f"Number of lines in {filename}: {num_lines}")
