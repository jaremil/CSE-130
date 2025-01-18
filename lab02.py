import json

file_path = "../lab02.json"

try:
    with open(file_path, 'r') as file:
        data = file.read()
        json_data = json.loads(data)
        # print(json_data)
except FileNotFoundError:
    print("Unable to open file Lab02.json.")
except OSError:
    print("Unable to open file Lab02.json.")

separated_list = list(json_data.values())

# print("Separated List:", separated_list)

usernames = json_data["username"]
passwords = json_data["password"]
input_user = input("Enter a Username: ")
input_pass = input("Enter a Password: ")

if input_user in usernames and input_pass in passwords:
    user_index = usernames.index(input_user)
    pass_index = passwords.index(input_pass)

    if user_index == pass_index:
        print("You are authenticated!")
    else:
        print("You are not authorized to use the system.")
else:
    print("You are not authorized to use the system.")