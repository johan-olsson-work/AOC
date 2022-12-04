# adding AOC folder to the system path
import sys
sys.path.insert(0, '/Users/johanol/repos/privat/AOC')
from helpers import common_functions

data = common_functions.get_data_once(day=4, year=2022)

input_data =  common_functions.get_array_of_strings(data)
print(f"input_data: {input_data}")

test_data = [
    '2-4,6-8',
    '2-3,4-5',
    '5-7,7-9',
    '2-8,3-7',
    '6-6,4-6',
    '2-6,4-8',
]

print(f"test_data: {test_data}")


def overlapp(range1, range2):
    for number in range_1:
        if number in range_2:
            return True
    return False

score = 0
for row in input_data:
    key, val = row.split(',')
    print(f"key: {key} and {val}")
    key_values = key.split('-')
    val_values = val.split('-')
    
    print(f"key_values: {key_values}")
    print(f"val_values: {val_values}")
    range_1 = range(int(key_values[0]), int(key_values[1]) + 1)
    range_2 = range(int(val_values[0]), int(val_values[1]) + 1)
    print(f"range_1: {range_1}")
    print(f"range_2: {range_2}")

    if overlapp(range_1, range_2) or overlapp(range_2, range_1):
        
        score += 1
    






print(f"score: {score}")

from aocd import submit
submit(score, part="b", day=4, year=2022)




