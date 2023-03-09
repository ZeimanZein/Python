#Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce


numbers = [2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)

print(product)
