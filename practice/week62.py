import re

email_pattern = r'\b[A-Za-z0-9._%+-]+@(mail|yahoo|bk)\.([A-Z|a-z]{2,})\b'

domain_map = {
    'mail': 'gmail',
    'yahoo': 'outlook',
    'bk': 'kbtu'
}
string = input("Enter a string: ")
def replace_domain(match):
    old_domain = match.group(1)
    new_domain = domain_map.get(old_domain, old_domain)
    return f"{match.group(0).replace(old_domain, new_domain)}"
new_string = re.sub(email_pattern, replace_domain, string)

print("New string:")
print(new_string)