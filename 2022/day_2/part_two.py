# adding AOC folder to the system path
import sys
sys.path.insert(0, '/Users/johanol/repos/privat/AOC')
from helpers import common_functions

data = common_functions.get_data_once(day=2, year=2022)

#print(f"data: {data}\n\n")
#print(f"lines(data): {common_functions.get_array_of_strings(data)}\n\n")
#print(f"lines(data): {common_functions.get_elf_cal_arr_tuple(data)}\n\n")
#print(f"lines(data): {}\n\n")

input_data = common_functions.get_array_of_string_tuplets(data)
test_data = [('A','Y'), ('B','X'), ('C','Z')]

#print(f"input_data: {input_data}")

def is_draw(opponent, player):
    return get_RPS(opponent) == get_RPS(player)

def is_win(opponent, player):
    if get_RPS(opponent) == 'ROCK' and get_RPS(player) == 'PAPER':
        return True
    if get_RPS(opponent) == 'PAPER' and get_RPS(player) == 'SISSORS':
        return True
    if get_RPS(opponent) == 'SISSORS' and get_RPS(player) == 'ROCK':
        return True
    return False

def get_win_draw_score(opponent, player):
    # Draw
    if is_draw(opponent, player):
        return 3
    # Win
    if is_win(opponent, player):
        return 6
    # Loss
    return 0

def get_challenger_choise(opponent, challenger):
    # To be refactored...
    if challenger == 'X':
        if opponent == 'A':
            challenger_new = 'Z'
        if opponent == 'B':
            challenger_new = 'X'
        if opponent == 'C':
            challenger_new = 'Y'
    if challenger == 'Y':
        if opponent == 'A':
            challenger_new = 'X'
        if opponent == 'B':
            challenger_new = 'Y'
        if opponent == 'C':
            challenger_new = 'Z'
    if challenger == 'Z':
        if opponent == 'A':
            challenger_new = 'Y'
        if opponent == 'B':
            challenger_new = 'Z'
        if opponent == 'C':
            challenger_new = 'X'
    return challenger_new

def get_RPS(char):
    conversion_table = {'A': 'ROCK', 'X': 'ROCK', 'B':'PAPER', 'Y':'PAPER',  'C':'SISSORS', 'Z':'SISSORS'}
    return conversion_table[char]

score = 0
for opponent, player in input_data:
    player_new = get_challenger_choise(opponent, player)
    if get_RPS(player_new) == 'ROCK':
        score += 1
    if get_RPS(player_new) == 'PAPER':
        score += 2
    if get_RPS(player_new) == 'SISSORS':
        score += 3

    score += get_win_draw_score(opponent, player_new)

    
print(f"score: {score}")



# Try this for submitting...
#from aocd import submit
#submit(score, part="b", day=2, year=2022)
