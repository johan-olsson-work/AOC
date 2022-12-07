import os
from aocd import get_data
from aocd import submit

def get_data_once(day, year):
    if os.path.exists("input.txt"):
        with open("input.txt", "r") as f:
            lines = f.read()
    else:
        lines = get_data(day=day, year=year)
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
        if val <= 100000:
            size += val
    return size

def get_total_used_size(directory_sizes):
    return directory_sizes['/']

def get_size_left_on_device(used_size):
    return 70000000 - used_size

def calculate_size_of_dirs_to_remove(size_left, directory_sizes):
    sorted_directory_sizes = sorted(directory_sizes.items(), key=lambda x:x[1])
    for some_tuple in sorted_directory_sizes:
        if size_left + some_tuple[1] > 30000000:
            return some_tuple[1]

def part_two(input_data):
    directory_sizes = {}
    current_path = []
    for line in input_data:
        if is_command(line):
            if is_step_into(line):
                current_path.append(line.split()[2])           
            elif is_step_out(line):
                current_path.pop()
            elif is_goto_root(line):
                current_path = ['/']
        elif is_file(line):
            # Add size of file in current dir and all above
            for i in range(len(current_path)):
                key = get_as_path_string(current_path[:len(current_path)-i:])
                if key in directory_sizes:
                    directory_sizes[key] += get_file_size(line)
                else:
                    directory_sizes[key] = get_file_size(line)
        

    # Calculate size to remove
    used_size = get_total_used_size(directory_sizes)
    size_left = get_size_left_on_device(used_size)
    total_removed = calculate_size_of_dirs_to_remove(size_left, directory_sizes)
    
    return total_removed


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
    test_score = part_two(test_input)
    print(f"Test score: {test_score}")

    print()

    print(f"## PART 2 ##:")
    score = part_two(data.splitlines())
    print(f"score: {score}")

    #submit(score, part="b", day=7, year=2022)
