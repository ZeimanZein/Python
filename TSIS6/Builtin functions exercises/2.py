#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

string = input("Enter a string: ")

upper_count = 0
lower_count = 0

for char in string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
