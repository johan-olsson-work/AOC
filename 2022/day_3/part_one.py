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

def get_common_letters(part_one, part_two):
    common_letters = [x for x in part_one if x in part_two]

    return common_letters

def get_score_of_letter(char):
    scores = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
              'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
              'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38,
              'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52 }

    return scores[char]

def get_score_of_ascii(char):
    return ord(char) - 96 if char.islower() else ord(char) - 64 + 26
    
def get_part_of_string(string, from_char_nbr, to_char_nbr):
    string_slice = slice(from_char_nbr, to_char_nbr)  
    return string[string_slice]

score = 0
for line in input_data:
    part_one = get_part_of_string(line, 0, len(line) //2 ) # // for integer, / for double
    part_two = get_part_of_string(line, len(line) // 2, len(line))

    common_letters = get_common_letters(part_one, part_two)
    score += get_score_of_ascii(common_letters[0])
    
print(f"Total score: {score}")

