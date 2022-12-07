import os
from aocd import get_data
from aocd import submit

def get_data_once(day, year):
    if os.path.exists("input.txt"):
        with open("input.txt", "r") as f:
            lines = f.read()
    else:
        lines = get_data(day=day, year=year)
        #print(f"type(lines): {type(lines)}")

        with open("input.txt", "w") as f:
            for line in lines:
                f.write(line)
    return lines


def is_command(line):
    return line.split()[0] == '$'


def is_step_into(line):
    return line.split()[1] == 'cd' and line.split()[2] != '..' and line.split()[2] != '/'  

def is_step_out(line):
    return line.split()[1] == 'cd' and line.split()[2] == '..'

def is_goto_root(line):
    return line.split()[1] == 'cd' and line.split()[2] == '/'

def is_file(line):
    return line.split()[0].isdigit()

def get_as_path_string(path_list):
    return '/'.join(path_list)

def get_file_size(line):
    return int(line.split()[0])

def get_score(path_size_map):
    size = 0
    for key,val in path_size_map.items():
        #print(f"key: {key} val: {val}")

        if val <= 100000:
            size += val
    return size

def part_one(input_data):
    directory_sizes = {}
    current_path = []
    for line in input_data:
        #print(f"line: {line}")

        if is_command(line):
            #print(f"line is command: {line}")
            if is_step_into(line):
                #print(f"    line is step into: {line}")
                current_path.append(line.split()[2])           
            elif is_step_out(line):
                #print(f"    line is step out: {line}")
                current_path.pop()
            elif is_goto_root(line):
                #print(f"    goto root: {line}")
                current_path = ['/']
        elif is_file(line):
            #print(f"found file with size:: {get_file_size(line)}")

            # Add size of file in current dir and all above
            for i in range(len(current_path)):
                key = get_as_path_string(current_path[:len(current_path)-i:])
                if key in directory_sizes:
                    directory_sizes[key] += get_file_size(line)
                else:
                    directory_sizes[key] = get_file_size(line)
        
    # Calculate score
    return get_score(directory_sizes)


if __name__ == "__main__":
    data = get_data_once(7, 2022)
    
    #print(f"data: {data.splitlines()}")    
    
    test_input = ["$ cd /",
                  "$ ls",
                  "dir a",
                  "14848514 bcdb.txt",
                  "8504156 cdc.dat",
                  "dir d",
                  "$ cd a",
                  "$ ls",
                  "dir e",
                  "29116 f",
                  "2557 g",
                  "62596 h.lst",
                  "$ cd e",
                  "$ ls",
                  "584 i",
                  "$ cd ..",
                  "$ cd ..",
                  "$ cd d",
                  "$ ls",
                  "4060174 j",
                  "8033020 d.log",
                  "5626152 d.ext",
                  "7214296 k"]

    print(f"## TEST ##:")
    test_score = part_one(test_input)
    print(f"Test score: {test_score}")

    print()

    print(f"## PART 2 ##:")
    score = part_one(data.splitlines())
    print(f"score: {score}")

    #submit(score, part="a", day=7, year=2022)
