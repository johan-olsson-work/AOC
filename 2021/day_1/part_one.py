from aocd import get_data

# adding AOC folder to the system path
import sys
sys.path.insert(0, '/Users/johanol/repos/privat/AOC')
from helpers import transforms


data = get_data(day=1, year=2021)

print(f"data: {data}\n\n")
print(f"lines(data): {transforms.get_array_of_strings(data)}\n\n")
print(f"numbers(data): {transforms.get_array_of_numbers(data)}\n\n")

input_data = transforms.get_array_of_numbers(data)

# Part One
counter = 0
last = input_data[0]
for val in input_data:
    if val > last:
        counter += 1
    last = val

print(f"Answer: {counter}")

