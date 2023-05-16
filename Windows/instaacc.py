import random
import string

def generate_username():
    return ''.join(random.choices(string.ascii_lowercase, k=8))

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def generate_email():
    username = generate_username()
    domain = 'gmail'
    extension = 'com'
    return f"{username}@{domain}.{extension}"

def create_instagram_accounts(num_accounts):
    for _ in range(num_accounts):
        username = generate_username()
        password = generate_password()
        email = generate_email()

        # Code here to automate the account creation process
        # Bypassing security measures and terms of service

        print("New Instagram Account Created:")
        print("Username:", username)
        print("Password:", password)
        print("Email:", email)
        print("------------------------")

num_accounts = 5  # Change this value to the desired number of accounts
create_instagram_accounts(num_accounts)
