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


def is_overlap(range_1, range_2):
    # return len([x for x in range_1 if x in range_2]) > 0
    for number in range_1:
        if number in range_2:
            return True
    return False

score = 0
for pair_assignments in input_data:
    elf_1, elf_2 = pair_assignments.split(',')
    elf_1_assignments = elf_1.split('-')
    elf_2_assignments = elf_2.split('-')
    
    range_1 = range(int(elf_1_assignments[0]), int(elf_1_assignments[1]) + 1)
    range_2 = range(int(elf_2_assignments[0]), int(elf_2_assignments[1]) + 1)

    if is_overlap(range_1, range_2):
        score += 1
    

print(f"score: {score}")

#submit(score, part="b", day=4, year=2022)




