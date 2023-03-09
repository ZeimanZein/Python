#Write a Python program to write a list to a file.

my_list = ['apple', 'banana', 'orange', 'grape']

with open('my_file.txt', 'w') as file:

    for item in my_list:
        file.write(item + '\n')
        
