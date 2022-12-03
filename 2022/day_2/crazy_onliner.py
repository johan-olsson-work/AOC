# adding AOC folder to the system path
import sys
sys.path.insert(0, '/Users/johanol/repos/privat/AOC')
from helpers import common_functions

data = common_functions.get_data_once(day=2, year=2022)

#print(f"data: {data}\n\n")
#print(f"lines(data): {common_functions.get_array_of_strings(data)}\n\n")
#print(f"lines(data): {common_functions.get_elf_cal_arr_tuple(data)}\n\n")
#print(f"lines(data): {}\n\n")

input_data = common_functions.get_array_of_strings(data)

p1d = {'A X': 4, 'B X': 1, 'C X': 7, 'A Y': 8, 'B Y': 5, 'C Y': 2, 'A Z': 3, 'B Z': 9, 'C Z': 6}
p2d = {'A X': 3, 'B X': 1, 'C X': 2, 'A Y': 4, 'B Y': 5, 'C Y': 6, 'A Z': 8, 'B Z': 9, 'C Z': 7}
print(f"Part one:: {sum([p1d[line] for line in input_data])}")
print(f"Part two:: {sum([p2d[line] for line in input_data])}")
