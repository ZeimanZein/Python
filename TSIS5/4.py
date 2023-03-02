#Write a Python program to find the sequences of one upper case letter followed by lower case letters
import re

text = input()
patterns = '[A-Z]+[a-z]+$'
if re.search(patterns, text):
    print('There are matches')
else:
    print('No matches')