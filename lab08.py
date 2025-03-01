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

with open('Lab08.empty.json', 'rt') as file:
    data = file.read()
    empty_data = json.loads(data)
    empty_array = empty_data['array']

with open('Lab08.cities.json', 'rt') as file:
    data = file.read()
    cities_data = json.loads(data)
    cities_array = cities_data['array']

with open('Lab08.languages.json', 'rt') as file:
    data = file.read()
    languages_data = json.loads(data)
    languages_array = languages_data['array']

with open('Lab08.trivial.json', 'rt') as file:
    data = file.read()
    trivial_data = json.loads(data)
    trivial_array = trivial_data['array']

with open('Lab08.states.json', 'rt') as file:
    data = file.read()
    states_data = json.loads(data)
    states_array = states_data['array']


def sort(array):
    unsorted = len(array)

    while unsorted > 1:
        largest = array[0]
        largest_index = 0

        for i in range(1, unsorted):
            if array[i] > largest:
                largest = array[i]
                largest_index = i

        array[largest_index], array[unsorted -
                                    1] = array[unsorted - 1], array[largest_index]

        unsorted -= 1

    return array


print(sort(empty_array))
print(sort(cities_array))
print(sort(languages_array))
print(sort(trivial_array))
print(sort(states_array))
