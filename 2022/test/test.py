import pickle

# adding AOC folder to the system path
import sys
sys.path.insert(0, '/Users/johanol/repos/privat/AOC')
from helpers import common_functions

data = common_functions.get_data_once(day=1, year=2021)

print(f"data: {data}\n\n")
print(f"lines(data): {common_functions.get_array_of_strings(data)}\n\n")
print(f"numbers(data): {common_functions.get_array_of_numbers(data)}\n\n")

input_data = common_functions.get_array_of_numbers(data)


