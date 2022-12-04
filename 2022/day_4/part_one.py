# adding AOC folder to the system path
import sys
from aocd import submit

sys.path.insert(0, '/Users/johanol/repos/privat/AOC')
from helpers import common_functions

data = common_functions.get_data_once(day=4, year=2022)

input_data =  common_functions.get_array_of_strings(data)
#print(f"input_data: {input_data}")

test_data = [
    '2-4,6-8',
    '2-3,4-5',
    '5-7,7-9',
    '2-8,3-7',
    '6-6,4-6',
    '2-6,4-8',
]

print(f"test_data: {test_data}")

def is_range_subset(range_1, range_2):
    """Check if range_1 is a subset of range_2"""
    if not range_1:
        return True  # empty range is subset of anything
    if not range_2:
        return False  # non-empty range can't be subset of empty range
    if len(range_1) > 1 and range_1.step % range_2.step:
        return False  # must have a single value or integer multiple step
    return range_1.start in range_2 and range_1[-1] in range_2

score = 0
for pair_assignments in input_data:
    elf_1, elf_2 = pair_assignments.split(',')
    elf_1_assignments = elf_1.split('-')
    elf_2_assignments = elf_2.split('-')
    
    range_1 = range(int(elf_1_assignments[0]), int(elf_1_assignments[1]) + 1)
    range_2 = range(int(elf_2_assignments[0]), int(elf_2_assignments[1]) + 1)

    if is_range_subset(range_1, range_2) or is_range_subset(range_2, range_1):
        score += 1
    

print(f"score: {score}")

#submit(score, part="a", day=4, year=2022)




