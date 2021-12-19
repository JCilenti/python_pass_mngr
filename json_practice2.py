import json

data = {}
data['people'] = []
data['people'].append({
    'website': 'google.com',
    'username': 'jecilenti@gmail.com',
    'password': 'WestPoint1322'
})

data['people'].append({
    'website': 'facebook.com',
    'username': 'joeylovesbaseball@gmail.com',
    'password': 'Joey6870'
})

user_website = input("enter the name of a website: ")

for i in data.values():
    for u in i:
        user_data = list(u.values())
        #print(user_data[0])
        #print(user_data[1])
        print(user_data[2])
        # if user_website in user_data[0]:
        #     print(user_data)
        # #print(user_data)
        # else: 
        #     print("False")
#print(data['people'])
#print("*"*50)
#print(data['people'].pop(0))