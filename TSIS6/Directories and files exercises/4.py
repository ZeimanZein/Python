#Write a Python program to count the number of lines in a text file.
filename = input("Path: ")

with open(filename, 'r') as file:
    # Count the number of lines using a loop
    num_lines = 0
    for line in file:
        num_lines += 1

print(f"Number of lines in {filename}: {num_lines}")
