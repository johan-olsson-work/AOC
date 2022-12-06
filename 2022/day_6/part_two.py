import os
from aocd import get_data
from aocd import submit

def get_data_once(day, year):
    if os.path.exists("input.txt"):
        with open("input.txt", "r") as f:
            lines = f.read()
    else:
        lines = get_data(day=day, year=year)
        print(f"type(lines): {type(lines)}")

        with open("input.txt", "w") as f:
            for line in lines:
                f.write(line)
    return lines

def part_two(input_data):
    input_split = []
    for i, c in enumerate(input_data):
        if len(input_split) > 13:
            input_split.pop(0)
        input_split.append(c)
        if len(input_split) > 13:
            import collections
            # Check the length of an array with only unique duplicates, kind of overkill but it's what i found at the moment...
            if len(([item for item, count in collections.Counter(input_split).items() if count > 1])) == 0:
                return i
    

if __name__ == "__main__":

    data = get_data_once(6, 2022)

    score = part_two(data)
    print(f"score: {score + 1}")
