import os

path = input("Path:")

files = os.listdir(path)

python_files = [f for f in files if f.endswith('.py')]

for file in python_files:
    print(file)