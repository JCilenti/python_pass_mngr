import json


users = []
data = {}
data['users'] = []

site = input("Enter a website: ")
user = input("Enter a username: ")
passwd = input("Enter a password: ")

'''
data["users"].append({
	"website" : str(site),
        "username" : str(user),
        "password" : str(passwd)
        })
'''	
data.append({
	"website" : str(site),
        "username" : str(user),
        "password" : str(passwd)
})
with open('fake_accounts.txt', 'a') as out_file:
	json.dump(data, out_file)

