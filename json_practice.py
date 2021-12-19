import json

data = {}
data['people'] = []
data['people'].append({
    'website': 'google.com',
    'username': 'jecilenti@gmail.com',
    'password': 'WestPoint1322'
})

user_name = input("Enter your username: ")

def getDataByUsername():
    for i in data.values():
        for u in i:
            user_data = list(u.values())
            if user_name in user_data[1]:
                print("[FETCHING USER DATA...]")
                print(user_data)
            else:
                print("Data not found. [EXITING...]")


def getDataByPassword():
    for i in data.values():
        for u in i:
            user_data = list(u.values())
            if user_name in user_data[2]:
                print("[FETCHING USER DATA...]")
                print(user_data)
            else:
                print("Data not found. [EXITING...]")

def getDataByWebsite():
    for i in data.values():
        for u in i:
            user_data = list(u.values())
            if user_name in user_data[0]:
                print("[FETCHING USER DATA...]")
                print(user_data)
            else:
                print("Data not found. [EXITING...]")



if __name__ == '__main__':
    getDataByUsername()
    getDataByPassword()
    getDataByWebsite()