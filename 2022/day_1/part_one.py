import pickle

# adding AOC folder to the system path
import sys
sys.path.insert(0, '/Users/johanol/repos/privat/AOC')
from helpers import common_functions


def get_elf_cal_dict(array_of_cal):
    i = 1
    elfNbr_cal = {}
    for calories in array_of_cal:
        if calories:
            if i in elfNbr_cal:
                elfNbr_cal[i] += int(calories)
            else:
                elfNbr_cal[i] = int(calories)
        else:
            i+=1
    return elfNbr_cal


def get_elf_cal_arr_tuple(array_of_cal):
    i = 1
    elf_cal_array = []
    current_elf_cals = 0
    for calories in array_of_cal:
        if calories:
            current_elf_cals += int(calories)
        else:
            elf_cal_array.append((i,current_elf_cals))
            current_elf_cals = 0
            i+=1

    elf_cal_array.sort(key=lambda a: a[1])

    return elf_cal_array


data = common_functions.get_data_once(day=1, year=2022)
input_data = common_functions.get_array_of_strings(data)

elfs_cal_arr = get_elf_cal_arr_tuple(input_data)

print(f"elf_with_most_calories: {elfs_cal_arr[-1][0]}")
print(f"most_calories: {elfs_cal_arr[-1][1]}")
