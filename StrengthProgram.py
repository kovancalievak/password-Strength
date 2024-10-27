import re

password = input("Enter your password: ")
if len(password) < 8:
    print("Password must be at least 8 characters")
elif not re.search("[A-Z]", password):
    print("Password must contain at least one uppercase letter")
elif not re.search("[a-z]", password):
    print("Password must contain at least one lowercase letter")
elif not re.search("[0-9]", password):
    print("Password must contain at least one number")
elif not re.search("[^a-zA-Z0-9]", password):
    print("Password must contain at least one punctuation")
else:
    print("Password is strong")