

my_file = open("pass_file.txt", "a")

user_site = input("Enter the website: ")
user_name = input("Enter your username: ")
user_pass = input("Enter your password: ")

my_file.write("*" * 25 + "\n")
my_file.write("WEBSITE: {}\n".format(user_site))
my_file.write("USERNAME: {}\n".format(user_name))
my_file.write("PASSWORD: {}\n".format(user_pass))
my_file.write("*" * 25 + "\n\n")
my_file.close()

my_file = open("pass_file.txt", "r")

username_ask = input("Enter username to search for: ")

lines = my_file.readlines()
for i in lines:
	if username_ask in i:
		print("USERNAME EXISTS [FETCHING...]")
		print(i)
		
my_file.close()
