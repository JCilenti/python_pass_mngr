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
import json

users = {} 
data = {}
data["users"] = []
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
        print("[1] Search for Username")
        print("[2] Search for Password")
        print("[3] Search by website")
        print("[4] Enter New Credentials")
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
    if path.exists("passwords.txt"):
        print("File exists")
        outfile = open("passwords.txt", "a")
    else:
        print("[CREATING FILE...]")
        out_file = open("passwords.txt", "a")
        out_file.close()

def checkUser():
    if checkAccess(username_original, password_original) == 0:
        promptUser()
    else:
        print("Denied Access")

def promptUser():
    user_input = input("Select a choice from the list: ")
    if int(user_input) == 1:
        print("getting your username")
        getCredentials()
    elif int(user_input) == 2:
        print("getting your password")
        getCredentials()
    elif int(user_input) == 3:
        print("Searching by website")
        getCredentials()
    elif int(user_input) == 4:
        print("Adding new credentials")
        addCredentials()
    else:
        print("Choice out of range. [Exiting...]")
        return int(user_input)

def getCredentials():
    # The index key or value will be either password or username
    # Based on the choice of the user, return either key or value
    print("getting your username for you")
    

def websiteSearch():
    # this will be some index in the JSON file
    # once webiste is found, present user with website, username and password
    print("Getting credentials website")

def addCredentials():
    # prompt user for webiste, username, and password
    # individually write these to a line in the JSON file
    # file must be opened, written to, and closed
    os.system('clear')
    site = input("Enter the name of the wesbite or app: ")
    os.system('clear')
    user = input("Enter your username: ")
    os.system('clear')
    passwd = input("Enter your password: ")
    passwd2 = input("Re-enter your password: ")
    os.system('clear')
    if passwd == passwd2:
        print("Credentials entered successfully. [SAVING...]")
        data["users"].append({
            "website" : str(site),
            "username" : str(user),
            "password" : str(passwd)
            })
        with open('passwords.txt', 'a') as outfile:
            json.dump(data, outfile)
        # there should also be a check for whether creds exist already
        # save to file here
        # call file saving function
    else:
        print("Passwords do not match.")
        passwd2 = input("Please Re-enter your password: ")

# def savetoFile()
    # this function will save creds to JSON passwords file


# check number of occurences of password
    # iterate through file with for loop
    # create a counter to increment if key == certain value
    # compare count to secure value
# if password more than a certain number
# print bad security in terminal and highlight or something

# add a system that checks the user's entered password against personal security
# does it have 15 characters? symbols? letters and numbers?


if __name__== "__main__":
    printBanner()
    checkFile()
    checkUser()
    #print(promptUser())
    #if checkAccess(username_original, password_original) == 0:
        #promptUser()







