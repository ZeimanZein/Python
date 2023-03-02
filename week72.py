import os

path = input("Path:")

files = os.listdir(path)

python_files = [f for f in files if f.endswith('.py')]

for file in python_files:
    print(file)
    
filename = input("Name of file:")

with open(os.path.join(path, filename), 'r') as f:
    data = f.read()

print(f"Data in {filename}:")
print(data)

num_chars = len(data)
num_functions = data.count('def')
num_equals = data.count('=')
print(f"Number of characters:{num_chars}")
print(f"Number of function:{num_functions}")
print(f"Number of equals:{num_equals}")