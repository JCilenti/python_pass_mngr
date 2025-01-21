import os.path
from os import path
import hashlib
import json

users = {}
data = {}
data["users"] = []

def check_for_creds():
    # use will need to add a file to their system called creds
    # this file will contain username and password separated by comma
    # this function will look for this file and read it

    #creds_file_dir = input("Please enter your creds file directory: ")
    # '../../creds.txt'
    creds_file = open('../../creds.txt', 'r')
    #creds_file = open(creds_file_dir, 'r')
    password = creds_file.readlines(1)[0]
    #print(password)
    creds_file.close()

    username = input("Please enter your username: ")
    ask_password = input("Please enter your password: ")
    #print(ask_password)
    #print(len(password))
    #print(len(ask_password))

    if ask_password == password:
        os.system('clear')
        print("***** Welcome {} *****".format(username))
        prompt()
    else:
        print("Username or password is incorrect!")
        return 0

    
def prompt():
    print("The Following Options are Below")
    print("[1] Search for Username")
    print("[2] Search for Password")
    print("[3] Search by website")
    print("[4] Enter New Credentials")
    print("[5] Create Your Password File")
    print("[6] Quit Program")
    user_prompt_response()


def user_prompt_response():
    user_choice = input("Select a choice from the list: ")
    user_choice = int(user_choice)

    if user_choice == 1:
        os.system('clear')
        print("[GETTING DATA BY USERNAME...]")
        os.system('clear')
        #getCredentialsUser()
    if user_choice == 2:
        print("[GETTING DATA BY PASSWORD...]")
        os.system('clear')
        #getCredentialsPass()
    if user_choice == 3:
        print("[SEARCHING BY KEYWORD...]")
        os.system('clear')
        #getCredentialsWeb()
    if user_choice == 4:
        print("[ADDING NEW CREDENTIALS...]")
        os.system('clear')
        addCredentials()
    if user_choice == 5:
        print("[CREATING PASSWORDS FILE...]")
        os.system('clear')
        checkFile()
    if user_choice == 6:
        print("[QUITTING...]")
        print("GOODBYE!")
        exit()
        

def printBanner():
    print("#"*50)
    print("#" + " "*48 + "#")
    print("#" + " "*7 + "WELCOME TO PYTHON PASSWORD MANAGER" + " "*7 + "#")
    print("#" + " "*48 + "#")
    print("#"*50)
    
    lock_banner = """
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMWNKOOOOKNWMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMXkc,......,ckXMMMMMMMMMMMMM
    MMMMMMMMMMMMKc..'cdxxdc'..cKMMMMMMMMMMMM
    MMMMMMMMMMMXc..:0WMMMMW0:..cXMMMMMMMMMMM
    MMMMMMMMMMM0,.'kMMMMMMMMk'.,0MMMMMMMMMMM
    MMMMMMMMMMMO,..dXXXXXXXXd..,OMMMMMMMMMMM
    MMMMMMMMMNk;....''''''''....;kNMMMMMMMMM
    MMMMMMMMMO,..................,OMMMMMMMMM
    MMMMMMMMMO'......,oddo,......'OMMMMMMMMM
    MMMMMMMMMO'......dNMMNd......'OMMMMMMMMM
    MMMMMMMMMO'......,OWWO,......'OMMMMMMMMM
    MMMMMMMMMO'.......xWWx.......'OMMMMMMMMM
    MMMMMMMMMO'.......cOOc.......'OMMMMMMMMM
    MMMMMMMMM0:..................:0MMMMMMMMM
    MMMMMMMMMWKdccc::::::::::cccdKWMMMMMMMMM
    MMMMMMMMMMMMMWWWWWWWWWWWWWWMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    """
    print(lock_banner)

def checkFile():
    # user enters path to passwords file
    #../../passwords.txt
    password_location = input("Enter the location of your passwords file: ")
    if path.exists(password_location):
        print("File exists")
        os.system('clear')
        prompt()
        #out_file = open("passwords.txt", "a")
    else:
        print("[CREATING FILE...]")
        #out_file = open("passwords.txt", "a")
        new_passwords_file = open("../../passwords.json", "w")
        #welcome_str = "##### This is the Password File #####\n"
        #out_file.write(welcome_str)
        new_passwords_file.close()


# Its time to start handling input
# Experiment with JSON



def addCredentials():
    # open json file
    # ask user for site, username, and pass
    # write to file
    # close file
    site = input("Enter website or source: ")
    user = input('Enter username: ')
    passw = input('Enter password: ')

    creds_dict = {
        "site": site,
        "username": user,
        "password": passw
    }

    print("Is this the correct data to be entered: ")
    print(creds_dict)
    response = input("y/n?: ")
    if response == "y":
        # serialize the data to be written to json file
        json_creds = json.dumps(creds_dict, indent=4)

        # write to json now
        with open('../../passwords.json', 'a') as pass_file:
            pass_file.write(json_creds)
            print("[CREDENTIALS ENTERED SUCCESSFULLY...]")
        # return to home screen here
    else: 
        os.system('clear')
        addCredentials()
'''
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



def getCredentialsUser():
    # The index key or value will be either password or username
    # Based on the choice of the user, return either key or value
    username_ask = input("Enter username to search: ")
    with open("passwords.txt") as out_file:
        if os.stat("passwords.txt").st_size == 0:
            print("File is Empty! [CLOSING...]")
            printBanner()
            promptUser()
            # prompt the user if they would like to add creds here
            # THIS IS UNNECESSARY
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


# check number of occurences of password
    # iterate through file with for loop
    # create a counter to increment if key == certain value
    # compare count to secure value
# if password more than a certain number
# print bad security in terminal and highlight or something

# add a system that checks the user's entered password against personal security
# does it have 15 characters? symbols? letters and numbers?

'''

if __name__== "__main__":
    printBanner()   
    check_for_creds()
    #user_prompt_response()
    #checkFile()
    #checkUser()




    #print(promptUser())
    #if checkAccess(username_original, password_original) == 0:
        #promptUser()







