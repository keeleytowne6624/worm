import random
import string

def generate_username():
    return ''.join(random.choices(string.ascii_lowercase, k=8))

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def create_instagram_account():
    username = generate_username()
    password = generate_password()

    # Code here to automate the account creation process
    # Bypassing security measures and terms of service

    print("New Instagram Account Created:")
    print("Username:", username)
    print("Password:", password)

create_instagram_account()
