import json

file_path = "../lab02.json"

try:
    with open(file_path, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Unable to open file Lab02.json.")
except OSError:
    print("Unable to open file Lab02.json.")


with open ('lab02.json', "wt") as filehandle:
    json.dump('lab02.json', filehandle)

with open('lab02.json', "rt") as filehandle:
    data = filehandle.read()
    print(data)
    data_dictionary = json.loads(data)
    print(data_dictionary['name'] + 'worked!!')
