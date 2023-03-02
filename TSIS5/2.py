#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

text = input()
patterns = 'ab{2,3}'
if re.search(patterns,  text):
    print('There are matches')
else:
    print('No matches')