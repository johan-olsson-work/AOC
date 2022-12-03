# adding AOC folder to the system path
import sys
sys.path.insert(0, '/Users/johanol/repos/privat/AOC')
from helpers import common_functions

data = common_functions.get_data_once(day=2, year=2022)

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

def get_RPS(char):
    conversion_table = {'A': 'ROCK', 'X': 'ROCK', 'B':'PAPER', 'Y':'PAPER',  'C':'SISSORS', 'Z':'SISSORS'}
    return conversion_table[char]

score = 0
for opponent, player in input_data:
    if get_RPS(player) == 'ROCK':
        score += 1
    if get_RPS(player) == 'PAPER':
        score += 2
    if get_RPS(player) == 'SISSORS':
        score += 3

    score += get_win_draw_score(opponent, player)

    
print(f"score: {score}")




