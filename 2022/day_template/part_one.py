# adding AOC folder to the system path
import sys
from aocd import submit

sys.path.insert(0, '/Users/johanol/repos/privat/AOC')
from helpers import common_functions

data = common_functions.get_data_once(day=x, year=2022)

input_data = common_functions.get_array_of_numbers(data)
print(f"input_data_numbers: {input_data}")
print("")

input_data = common_functions.get_array_of_strings(data)
print(f"input_data_strings: {input_data}")
print("")

input_data = common_functions.get_array_of_string_tuplets(data, separator=' ')
print(f"input_data_string_tuplets: {input_data}")
print("")

input_data = common_functions.get_array_of_dict_strings(data, separator=' ')
print(f"input_data_dict_strings: {input_data}")
print("")

input_data = common_functions.get_array_of_dict_ints(data, separator=' ')
print(f"input_data_dict_ints: {input_data}")
print("")



# test_data = [
# ]
# print(f"test_data: {test_data}")



if __name__ == "__main__":
    score = 0










    print(f"score: {score}")

    #submit(score, part="a", day=x, year=2022)




