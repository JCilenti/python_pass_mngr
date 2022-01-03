'''
Python Based Password Manager

- [x] Enter email and password
- [x] Save/append to file
- [x] Create new file if one doesn't exist
- [x] Enter password to access
    - [x] If wrong password, prompt
    - [x] Correct -> Send user to options
- [x] Provide user with options
    - [x] Enter website to see username/password
    - [x] Quit program with "q"
- [ ] Create a way to encrypt or secure the passwords.json file

** Problems to address:
1. When adding new credentials to the file, it creates a whole new 
   version of the dictionary. How to stop this from happening?
      - copy file contents, re-write file with new contents?
      - append but make append actually work
2. When new file is created, it appends to a dictonary that doesn't 
   exist. 
   The file has to be opened with 'w' but appended with add creds

3. What if I indexed the value of user for the dict. Every time a new 
   entry is made,
   a new dict structure is created (Ex. dict[user1]=[], dict[usern]=[]
   
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
        print("[5] Quit Program")
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
        #out_file = open("passwords.txt", "a")
    else:
        print("[CREATING FILE...]")
        #out_file = open("passwords.txt", "a")
        out_file = open("passwords.txt", "w")
        #welcome_str = "##### This is the Password File #####\n"
        #out_file.write(welcome_str)
        out_file.close()

def checkUser():
    if checkAccess(username_original, password_original) == 0:
        promptUser()
    else:
        print("Denied Access")

def promptUser():
    user_input = input("Select a choice from the list: ")
    if int(user_input) == 1:
        print("[GETTING DATA BY USERNAME...]")
        os.system('clear')
        getCredentialsUser()
    elif int(user_input) == 2:
        print("[GETTING DATA BY PASSWORD...]")
        os.system('clear')
        getCredentialsPass()
    elif int(user_input) == 3:
        print("[SEARCHING BY KEYWORD...]")
        os.system('clear')
        getCredentialsWeb()
    elif int(user_input) == 4:
        print("[ADDING NEW CREDENTIALS...]")
        os.system('clear')
        addCredentials()
    elif int(user_input) == 5:
        print("[QUITTING...]")
        print("GOODBYE!")
        exit()
    else:
        print("Choice out of range. [Exiting...]")

def getCredentialsUser():
    # The index key or value will be either password or username
    # Based on the choice of the user, return either key or value
    username_ask = input("Enter username to search: ")
    with open("passwords.txt") as out_file:
        if os.stat("passwords.txt").st_size == 0:
            print("File is Empty! [CLOSING...]")
            # prompt the user if they would like to add creds here
        else:
            data = json.load(out_file)
            for i in data.values():
                for u in i:
                    user_data = list(u.values())
                    #if username_ask in user_data[1]:
                    if username_ask in user_data[1]:
                        print("[FETCHING USER DATA...]")
                        print(user_data)
                    else:
                        print("Data not found. [EXITING...]")

def getCredentialsPass():
    # The index key or value will be either password or username
    # Based on the choice of the user, return either key or value
    password_ask = input("Enter password to search: ")
    with open("passwords.txt") as out_file:
        data = json.load(out_file)
        for i in data.values():
            for u in i:
                user_data = list(u.values())
                if password_ask in user_data[2]:
                    print("[FETCHING USER DATA...]")
                    print(user_data)
                else:
                    print("Data not found. [EXITING...]")

def getCredentialsWeb():
    # The index key or value will be either password or username
    # Based on the choice of the user, return either key or value
    website_ask = input("Enter website to search: ")
    with open("passwords.txt") as out_file:
        data = json.load(out_file)
        for i in data.values():
            for u in i:
                user_data = list(u.values())
                if website_ask in user_data[0]:
                    print("[FETCHING USER DATA...]")
                    print(user_data)
                else:
                    print("Data not found. [EXITING...]")    

def addCredentials():
    # prompt user for webiste, username, and password
    # individually write these to a line in the JSON file
    # file must be opened, written to, and closed
    with open('passwords.txt') as out_file:
        data = json.load(out_file)
        os.system('clear')
        site = input("Enter the name of the wesbite or app: ")
        for i in data.values():
            for u in i:
                user_data = list(u.values())
                if site in user_data[0]:
                    print("Credentials exist for this site")
                    print(user_data[0])
                    print("Would you like to modify credentials?")
                    user_decision = input("y/n: ")
                    if user_decision == "y":
                        # remove either password, website, or username
                        # -1 = pass
                        # -2 = user
                        # -3 = website
                        del_items = input("Remove Website, User, Pass or All?: ")
                        if del_items == "website":
                            user_data.pop(-3)
                            new_website = input("Enter new website: ")
                            data['users'].append({
                                "website" : str(new_website)
                            })
                            exit()
                        
                    else:
                        continue
                else:
                    continue
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
        with open('passwords.txt', 'a') as out_file:
            json.dump(data, out_file)
        # there should also be a check for whether creds exist already
        # save to file here
        # call file saving function
    else:
        print("Passwords do not match.")
        passwd2 = input("Please Re-enter your password: ")
        print("Credentials entered successfully. [SAVING...]")
        data["users"].append({
            "website" : str(site),
            "username" : str(user),
            "password" : str(passwd)
            })
        with open('passwords.txt', 'a') as out_file:
            json.dump(data, out_file)

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







