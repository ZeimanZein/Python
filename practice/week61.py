import re

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

string = input("Enter a string: ")

email_addresses = re.findall(email_pattern, string)

print("Email addresses: ")
for email in email_addresses:
    print(email)