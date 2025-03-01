# 1. Name:
#      Jade Miller
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This is a Sort Algorithim. It arranges elements of a list in ascending order.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was ensuring that there were no bugs in the code and that the code was accurate to the Puesdocode.
# 5. How long did it take for you to complete the assignment?
#      4

import json 

with open('Lab08.empty.json', 'r') as file:
    empty_data = json.load(file)
with open('Lab08.cities.json', 'r') as file:
    cities_data = json.load(file)
with open('Lab08.languages.json', 'r') as file:
    languages_data = json.load(file)
with open('Lab08.trivial.json', 'r') as file:
    trivial_data = json.load(file)
with open('Lab08.states.json', 'r') as file:
    states_data = json.load(file)

print(empty_data)
print(cities_data)
print(languages_data)
print(trivial_data)
print(states_data)

# FOR i_pivot <- array.length-1 ...0

#     i_largest <- 0

#     FOR i_check <- 1 ... i_pivot-1
    #       IF array[i_check] > array[i_largest]
    #           i_largest <- i_check
    #   IF array[i_largest] > array[i_pivot]
    #       SWAP array[i_largest] and array[i_pivot]
      
for 