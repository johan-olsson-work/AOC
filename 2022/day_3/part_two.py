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
print(f"input_data: {test_data}")

def get_common_letters(part_one, part_two):
    common_letters = []
    for c in part_one:
        if c in part_two:
            common_letters.append(c)
    print(f"common_letters: {common_letters}")
    return common_letters

def get_score_of_letter(c):
    scores = {'a': 1,
             'b': 2,
             'c': 3,
             'd': 4,
             'e': 5,
             'f': 6,
             'g': 7,
             'h': 8,
             'i': 9,
             'j': 10,
             'k': 11,
             'l': 12,
             'm': 13,
             'n': 14,
             'o': 15,
             'p': 16,
             'q': 17,
             'r': 18,
             's': 19,
             't': 20,
             'u': 21,
             'v': 22,
             'w': 23,
             'x': 24,
             'y': 25,
             'z': 26,
             'A': 27,
             'B': 28,
             'C': 29,
             'D': 30,
             'E': 31,
             'F': 32,
             'G': 33,
             'H': 34,
             'I': 35,
             'J': 36,
             'K': 37,
             'L': 38,
             'M': 39,
             'N': 40,
             'O': 41,
             'P': 42,
             'Q': 43,
             'R': 44,
             'S': 45,
             'T': 46,
             'U': 47,
             'V': 48,
             'W': 49,
             'X': 50,
             'Y': 51,
             'Z': 52
             }
    print(f"scores[c]: {scores[c]}")

    return scores[c]
    

# Get groups
groups = []
popped_list = test_data

#values = set(map(lambda x:x[1], mylist))
#newlist = [[y[0] for y in mylist if y[1]==x] for x in values]

#for i, line in enumerate(test_data):
#    for c in line:
#        for rest_of_lines in 
#        if any(c in line for x in line): ...
#        
#    for pop_line in popped_list:
#        common_letters = get_common_letters(line, pop_line) 
#        if common_
import itertools
for a, b in itertools.combinations(test_data, 2):
    #c = compare(a, b)
    print(f"a: {a}")
    print(f"b: {b}")
    for c in a:
        if c in b:
            print(f"Found matching {c} IN {a} AND {b}")

score = 0
for line in test_data:

    string1 = slice (0, len (line) //2)
    string2 = slice(len(line)//2, len(line))
    part_one = line[string1]
    part_two = line[string2]
    print(f"string1: {part_one}")
    print(f"string2: {part_two}")
    
    common_letters = get_common_letters(part_one, part_two)
    score += get_score_of_letter(common_letters[0])

def get_group_score(a,b,c):
    group_score = 0    
    for char in a:
        if char in b and char in c:
            group_score = get_score_of_letter(char)
    return group_score
    
group_score = 0
while input_data:
    a = input_data.pop()
    b = input_data.pop()
    c = input_data.pop()
    group_score += get_group_score(a,b,c)
    print(f"group_score: {group_score}")

print(f"group_scopre: {group_score}")
