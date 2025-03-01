# NOT COMPLETE

# with open("file.json", "wt") as f:
#     f.write('{\n\t"Firstname Lastname":\n}')

# f = open("file.txt","r")
# print(f.read())


import json

my_friend = {"Name" : "Jennie",
            "Phone" : "(123)456-7890",
            "Address" : "1111 Steet, City State ZIP",
            "Email" : "jennie@gmail.com" }

with open ('jan16_class.json', "wt") as filehandle:

    # THIS CREATES THE JSON FILE AND PUTS IT INTO A DICTIONARY
    # data_json = json.dumps(my_friend)
    # print(data_json)
    # filehandle.write(data_dictionary)

    # THIS CREATES THE JSON FILE AND PUTS IT INTO A DICTIONARY IN ONE LINE
    json.dump(my_friend, filehandle)

with open('jan16_class.json', "rt") as filehandle:
    data = filehandle.read()
    print(data)
    data_dictionary = json.loads(data)
    print(data_dictionary['name'] + 'worked!!')









# for(i = 1; i < length; i++) 
#     asserts(array[i -1 <= array[i]]);

# python version??
# for i in range(1, len(array)):
#     assert array[i - 1] <= array[i], "Array is not sorted!"
