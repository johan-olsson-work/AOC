import pickle

# adding AOC folder to the system path
import sys
sys.path.insert(0, '/Users/johanol/repos/privat/AOC')
from helpers import common_functions

data = common_functions.get_data_once(day=1, year=2022)

#print(f"data: {data}\n\n")
#print(f"lines(data): {common_functions.get_array_of_strings(data)}\n\n")
#print(f"numbers(data): {common_functions.get_array_of_numbers(data)}\n\n")

input_data = common_functions.get_array_of_strings(data)

print(f"input_data: {input_data}")

test_data = ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000']

elfNbr_cal = {}
i = 1

for calories in input_data:
    print(f"calories: {calories}")

    if calories:
        if i in elfNbr_cal:
            elfNbr_cal[i] += int(calories)
        else:
            elfNbr_cal[i] = int(calories)

    else:
        i+=1
            
print(f"elfNbr_cal: {elfNbr_cal}")

# Find maximum:
elf_with_most_calories = 0
most_calories = 0
for key, val in elfNbr_cal.items():
    print(f"Testing key: {key}, val: {val}")

    if val > most_calories:
        print("FOUND")
        most_calories = val
        elf_with_most_calories = key

print(f"elf_with_most_calories: {elf_with_most_calories}")
print(f"most_calories: {most_calories}")

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

#test_input =
#1000
#2000
#3000
#
#4000
#
#5000
#6000
#
#7000
#8000
#9000
#
#10000
#
