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


def range_subset(range1, range2):
    """Whether range1 is a subset of range2."""
    if not range1:
        
        return True  # empty range is subset of anything
    if not range2:
        return False  # non-empty range can't be subset of empty range
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 and range1[-1] in range2

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

    if range_subset(range_1, range_2) or range_subset(range_2, range_1):
        
        score += 1
    






print(f"score: {score}")

from aocd import submit
submit(score, part="a", day=4, year=2022)




