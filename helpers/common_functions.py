import os.path
import re
from aocd import get_data
import pickle

# For one value per row:
def get_array_of_strings(data):
    return data.splitlines()


def get_array_of_numbers(data):
    result = []
    for line in data.splitlines():
        matches = [int(n) for n in re.findall(r"-?\d+", line)]
        if matches:
            result.append(matches)
    if all(len(n) == 1 for n in result):
        # flatten the list if there is always 1 number per line
        result = [n for [n] in result]
    if len(result) == 1:
        # un-nest the list if there is only one line
        [result] = result
    return result

# For two values per row
def get_array_of_string_tuplets(data, separator=' '):
    result = []
    for row in data.splitlines():
        (key, val) = row.split(separator)
        result.append((key, val))
    return result

def get_array_of_dict_strings(data, separator=' '):
    result = []
    for row in data.splitlines(): 
        key, val = row.split(separator)
        result.append({key:val})
    return result

def get_array_of_dict_ints(data, separator=' '):
    result = []
    for row in data.splitlines(): 
        key, val = row.split(separator)
        result.append({key:int(val)})
    return result

def save_data(obj):
    print("Saving data to pickle")
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

def load_data():
    print("Loading data from pickle")
    try:
        with open("data.pickle", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


def get_data_once(day, year):
    if os.path.exists("data.pickle"):
        return load_data()
    else:
        data = get_data(day=day, year=year)
        save_data(data)
        return data
