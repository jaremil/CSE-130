# 1. Name:
#      Jade Miller
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program is able to check multiple JSON files for specific data. It will return true or false if the data searched is in the specific JSON file.
# 4. Algorithmic Efficiency
#     -Identify the algorithmic efficiency and tell why it is as you say it is-



# 5. What was the hardest part? Be as specific as possible.
#      The hardest part was identifying the algorithmic efficiency. The JSON files were all different sizes which helped determine how long it would take to search.
# 6. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import json 

with open('lab06.countries.json', 'r') as file:
    countries_data = json.load(file)
with open('lab06.empty.json', 'r') as file:
    empty_data = json.load(file)
with open('lab06.languages.json', 'r') as file:
    languages_data = json.load(file)
with open('lab06.trivial.json', 'r') as file:
    trivial_data = json.load(file)

print(countries_data)
print(empty_data)
print(languages_data)
print(trivial_data)


search_file = input("What is the name of the file? ")
search_word = input("What name are we looking for? ")

first = 0
last = len("array")
index = 0
thing = search_file(array[index])

while thing != search_word:
    index = round((first + last) / 2)
    index_item = 
# index_item ← item(letter_list[index])
# IF letter_index > index_item
# first ← index
# ELSE
# last ← index
# IF letter != index_item
# OUTPUT That letter is not in this list.
# ElSE
# OUTPUT Congratulations! You found the letter!