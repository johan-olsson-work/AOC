import pickle

# adding AOC folder to the system path
import sys
sys.path.insert(0, '/Users/johanol/repos/privat/AOC')
from helpers import common_functions

data = common_functions.get_data_once(day=3, year=2022)
input_data = common_functions.get_array_of_strings(data)
#print(f"input_data: {input_data}")

test_data=[
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw',
]


def get_group_score_old_readable(a,b,c):
    group_score = 0    
    for char in a:
        if char in b and char in c:
            group_score = get_score_of_ascii(char)
    return group_score

def get_score_of_ascii(char):
    return ord(char) - 96 if char.islower() else ord(char) - 64 + 26

def get_group_score(a,b,c):
    return [get_score_of_ascii(char) for char in a if char in b and char in c][0] # Only one element needed
        
group_score = 0
while input_data:
    group_score += get_group_score(input_data.pop(), input_data.pop(), input_data.pop())

print(f"group_scopre: {group_score}")
