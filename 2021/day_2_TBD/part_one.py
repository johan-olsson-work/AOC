from aocd import get_data

# adding AOC folder to the system path
import sys
sys.path.insert(0, '/Users/johanol/repos/privat/AOC')
from helpers import transforms


data = get_data(day=4, year=2021)

print(f"data: {data}\n\n")
print(f"get_array_of_strings: {transforms.get_array_of_strings(data)}\n\n")
print(f"get_array_of_numbers: {transforms.get_array_of_numbers(data)}\n\n")
#print(f"get_array_of_string_tuplets: {transforms.get_array_of_string_tuplets(data)}\n\n")
#print(f"get_array_of_dict_strings: {transforms.get_array_of_dict_strings(data)}\n\n")
#print(f"get_array_of_dict_ints: {transforms.get_array_of_dict_ints(data)}\n\n")


# Part One

test = transforms.get_array_of_numbers(data)

print(f"test[0]: {test[0]}")

print(f"test[1]: {test[1]}")
