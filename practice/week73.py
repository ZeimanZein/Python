import os

path = input("Path: ")

files = os.listdir(path)

python_files = [f for f in files if f.endswith('.py')]

for file in python_files:
    print(file)
    
filename = input("Name of file:")

with open(os.path.join(path, filename), 'r') as f:
    data = f.readlines()

print(f"Data in {filename}:")

for line_num, line in enumerate(data):
    print(f"{line_num+1}: {line.strip()}")

while True:
    line_num = input("Line number: ")
    if line_num == '***':
        break
    line_num = int(line_num) - 1 
    
    new_line = input("Update line: ")
    data[line_num] = new_line
with open (filename, 'w') as f:
    f.writelines(data)


