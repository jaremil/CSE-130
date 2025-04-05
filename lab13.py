# 1. Name:
#      Jade Miller
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
# It will ask the user for a file with the data and ask the user for the size of the sub-array. 
# The output will be the average power.
# 4. What was the hardest part? Be as specific as possible.
#      These assignments have gotten easier over the semester. I have been able to turn Pseudocode into Python easier and easier thoughout the semester. That skill set I think is what has made the differenct here. 
# 5. How long did it take for you to complete the assignment?
# 4 hours

import json
import os

def main():
    os.system('clear')
    file = str(input("What is the name of the json file?: "))
    assert len(file) != 0 
    assert file.endswith('.json')
    with open(file=file, mode= "rt") as filehandle:
        data = filehandle.read()
        data_set = json.loads(data)
        array = data_set['array']
        subarray_length = int(input("Please enter a subarray length: "))
        assert subarray_length >= 0
        assert subarray_length < len(array)
        highest_average = 0
        subarray_average(array, subarray_length, highest_average)


def subarray_average(array, subarray_length, highest_average):
    for i in range(len(array) - subarray_length + 1):
        subarray = array[i:i + subarray_length]
        average = sum(subarray) / subarray_length
        if average > highest_average:
            highest_average = average

    print(f'{highest_average:.2f}')

main()