#Write a Python program with builtin function that returns True if all elements of the tuple are true.

my_tuple = (True, True, False, True)

if all(my_tuple):
    print("All elements are true")
else:
    print("Not all elements are true")
