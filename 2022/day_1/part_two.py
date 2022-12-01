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

# Find the three Elfs carrying the most Calories. How many total Calories is those Elfs carrying?

# Find maximum:
elfs_with_most_calories = []

for key, val in elfNbr_cal.items():
    if len(elfs_with_most_calories) < 3:
        print(f"Adding: ({key}, {val})")

        elfs_with_most_calories.append((key, val))
        elfs_with_most_calories.sort(key=lambda a: a[1])
    else:
        for i in range(3):
            if elfs_with_most_calories[i][1] < val:
                print(f"Popping: {elfs_with_most_calories[i]}")

                elfs_with_most_calories.pop(i)
                print(f"Adding: {(key,val)}")
                elfs_with_most_calories.append((key, val))
                elfs_with_most_calories.sort(key=lambda a: a[1])
                break
    
    print(f"elfs_with_most_calories: {elfs_with_most_calories}")
    print("")
    
print(f"elfs_with_most_calories: {elfs_with_most_calories}")

total = elfs_with_most_calories[0][1] + elfs_with_most_calories[1][1] + elfs_with_most_calories[2][1]
print(f"total: {total}")
