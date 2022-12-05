# adding AOC folder to the system path
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

def get_arranged_data(data):
    crate_part, rule_part = data.split("\n\n")
    arranged_crates = [[],[],[],[],[],[],[],[],[]]
    j = 0
    
    # Put the creates as lists in all_ceates
    # Get every 4th char from input
    for i in range(1, 289, 4):
        # Calculate an index for all_creates based on i and j
        index = (i + -3*j - 1) % 9
        crate = crate_part[i]

        # Dont add empty space
        if crate != ' ':
            arranged_crates[index].append(crate)

        j += 1
        

    # Need to revert order of crates since it was read in from top to bottom
    for i, arr in enumerate(arranged_crates):
        arranged_crates[i] = arr[::-1]



    rule_strings = rule_part.splitlines()
    rules = []
    import re
    for rule in rule_strings:
        # Remove words and create list of numbers 
        rule_string = rule.split(' ')[1:6:2]
        # convert the string numbers to ints
        rule_int = [int(n) for n in rule_string] 
        rules.append(rule_int)
        
    return arranged_crates, rules


def part_two(crates, rules):
    for rule in rules:
        # Move to
        crates[rule[2]-1].extend(crates[rule[1]-1][len(crates[rule[1]-1])-rule[0]:len(crates[rule[1]-1]):])

        # Move from
        crates[rule[1]-1] = crates[rule[1]-1][:len(crates[rule[1]-1])-rule[0]:]
        
    for crate in crates:
        print(f"Top crate:: {crate[-1]}")
        

if __name__ == "__main__":
    # Get data (looking like the input.txt file)
    data = get_data_once(5, 2022)

    # Add each row as strings to an array
    # data_strings = data.splitlines()

    crates, rules = get_arranged_data(data)

    part_two(crates, rules)
