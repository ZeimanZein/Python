#Write a Python program that matches a string that has
# an 'a' followed by zero or more 'b''s.
import re

text = input()
patterns = '^a(b*)$'

if re.search(patterns,  text):
    print('The are matches')
else:
    print('No matches')