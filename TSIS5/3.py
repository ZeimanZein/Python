#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

text = input()
patterns = '^[a-z]+_[a-z]+$'
if re.search(patterns,  text):
    print('There are matches')
else:
    print('No matches')