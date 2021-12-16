'''

Python Based Password Manager

- [x] Enter email and password
- [ ] Save/append to file
- [x] Create new file if one doesn't exist
- [x] Enter password to access
    - [x] If wrong password, prompt
    - [x] Correct -> Send user to options
- [x] Provide user with options
    - [ ] Enter website to see username/password
    - [ ] Quit program with "q"
- [ ] Create a way to encrypt or secure the passwords.json file


'''

import os.path
from os import path
import hashlib

users = {} 

# Add a user
username_original = 'atomas22' # The users username
password_original = 'Joey6870' # The users password

def checkAccess(username_original, password_original):
    salt = os.urandom(32) # A new salt for this user
    key = hashlib.pbkdf2_hmac('sha256', password_original.encode('utf-8'), salt, 100000)
    users[username_original] = { # Store the salt and key
        'salt': salt,
        'key': key
    }

    # Verification attempt
    username_unverified = input("USERNAME: ")
    password_unverified = input("PASSWORD: ")

    salt = users[username_original]['salt']
    #key = users[username_unverified]['key'] # there is a bug here for incorrect username
    key = users[username_original]['key']
    new_key = hashlib.pbkdf2_hmac('sha256', password_unverified.encode('utf-8'), salt, 100000)

    if key == new_key:
        os.system('clear')
        print("Welcome {}".format(username_unverified))
        print("Select a choice from the list: ")
        print("[1] Get a username")
        print("[2] Get a password")
        print("[3] Search by website")
        return 0
    else:
        print("Username or password is incorrect!")
        return 1

def printBanner():
    print("#"*50)
    print("#" + " "*48 + "#")
    print("#" + " "*7 + "WELCOME TO PYTHON PASSWORD MANAGER" + " "*7 + "#")
    print("#" + " "*48 + "#")
    print("#"*50)

def checkFile():
    if path.exists("passwords.json"):
        print("File exists")
    else:
        out_file = open("passwords.json", "a")
        out_file.write("##### Python Passwords File #####")
        out_file.close()

def promptUser():
    user_input = input("Select a choice from the list: ")
    return user_input
    # if user_input == 1:
    #     return 0
    # elif user_input == 2: 
    #     return 1
    # elif user_input == 3: 
    #     return 2
    # else:
    #     print("NO!!!!!!")


def checkUser():
    if checkAccess(username_original, password_original) == 0:
        print("Hello")
    else:
        print("Denied Access")

        #promptUser()
        #if promptUser() == 0:
            #print("Find username in JSON")
        #elif promptUser() == 1:
            #print("Find password in JSON")
        #elif promptUser() == 2:
            #print("Search by website")


# check number of occurences of password
    # iterate through file with for loop
    # create a counter to increment if key == certain value
    # compare count to secure value
# if password more than a certain number
# print bad security in terminal and highlight or something


if __name__== "__main__":
    printBanner()
    checkFile()
    checkUser()
    promptUser()

    #print(promptUser())
    #if checkAccess(username_original, password_original) == 0:
        #promptUser()







