import hashlib
import os

users = {} # A simple demo storage

# Add a user
username = 'atomas22' # The users username
password = 'Joey6870' # The users password

salt = os.urandom(32) # A new salt for this user
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
users[username] = { # Store the salt and key
    'salt': salt,
    'key': key
}

# Verification attempt 2 (correct password)
username = input("USERNAME: ")
password = input("PASSWORD: ")

salt = users[username]['salt']
key = users[username]['key']
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

if key == new_key:
    print("Welcome {}".format(username))
else:
    print("Username or password is incorrect!")

