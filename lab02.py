# 1. Name:

#      Jade Miller

# 2. Assignment Name:

#      Lab 02: Authentication

# 3. Assignment Description:

#      This prgram is designed to compare a username and a password listed in a Json file. It does this through reading the file from it's location in my computer's files. There are errors prepared to keep the code from crashing if something goes wrong.

# 4. What was the hardest part? Be as specific as possible.
# Was the syntax of Python the hardest part? If so, what part?
# Was there some aspect of the problem that was particularly difficult to solve?
# Was there an especially difficult bug? If so, how did you resolve it?
# Was there some difficulty with the instructions or any part of the problem definition?

#   I struggled the most with the syntax of Python. The hardest part of the program for me as using try and except. I had to do research into what errors to have it look for. I had also forgotten about try so I needed to do a lot of research to find what I needed to do.

# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

# 3 hours

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

# separated_list = list(json_data.values())

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