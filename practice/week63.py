import re

password = input("Enter a password: ")

password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,15}$"

forbidden_words = ["qwerty", "asd"]

if len(password) < 8 or len(password) > 15:
    print("Password must be between 8 and 15 characters long.")
elif any(word.lower() in password.lower() for word in forbidden_words):
    print("Password must not contain 'qwerty' or 'asd'.")
elif not re.match(password_pattern, password):
    print("Password must contain at least 1 capital letter, 1 small letter, 1 special symbol, and 1 number.")
else:
    print("Password is valid.")