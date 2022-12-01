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

# Part Two
counter = 0

slider = [input_data[0], input_data[1], input_data[2]]
print(f"slider:{slider}")
print(f"sum of slider:{sum(slider)}")

for val in input_data[3:]:
    current_sum = sum(slider)
    slider.append(val)
    slider.pop(0)
    if sum(slider) > current_sum:
        counter += 1

print(f"Answer: {counter}")
