import re

# Regular expression pattern for a valid email
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Prompt the user for input
user_email = input("Enter your email address: ")

# Validate the email using the regex
if re.match(email_pattern, user_email):
    print("This is a valid email address.")
else:
    print("This is not a valid email address.")
