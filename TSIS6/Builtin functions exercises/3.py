#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
string = input("Enter a string: ")

string = string.lower()

reverse_string = string[::-1]

if string == reverse_string:
    print("Palindrome")
else:
    print("Not a palindrome")
