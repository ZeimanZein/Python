#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

text = input()
patterns = 'a.*?b$'
if re.search(patterns, text):
    print('There are matches')
else:
    print('No matches')