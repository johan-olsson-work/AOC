# adding AOC folder to the system path
import sys
sys.path.insert(0, '/Users/johanol/repos/privat/AOC')
from helpers import common_functions

data = common_functions.get_data_once(day=4, year=2022)

input_data =  get_array_of_strings(data)
print(f"input_data_1: {input_data}")

input_data =  get_array_of_numbers(data)
print(f"input_data_2: {input_data}")

input_data =  get_array_of_string_tuplets(data, separator=' ')
print(f"input_data_3: {input_data}")

input_data =  get_array_of_dict_strings(data, separator=' ')
print(f"input_data_4: {input_data}")

input_data =  get_array_of_dict_ints(data, separator=' ')
print(f"input_data_5: {input_data}")

# test_data = 












score = 0




print(f"score: {score}")
# Try this for submitting...
#from aocd import submit
#submit(score, part="a", day=4, year=2022)




