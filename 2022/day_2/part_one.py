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

#This strategy guide predicts and recommends the following:

#In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
#In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
#The third round is a draw with 

    # The winner of the whole tournament is the player with the highest score.
    # Your total score is the sum of your scores for each round.
    # The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    # plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

def it_is_a_draw(oponent, challenger):
    if oponent == 'A' and challenger == 'X':
        return True
    if oponent == 'B' and challenger == 'Y':
        return True
    if oponent == 'C' and challenger == 'Z':
        return True
    return False
    
    
def get_win_draw_score(oponent, challenger):
    if it_is_a_draw(oponent, challenger):
        return 3
    if oponent == 'A':
        if challenger == 'Y':
            return 6
    if oponent == 'B':
        if challenger == 'Z':
            return 6
    if oponent == 'C':
        if challenger == 'X':
            return 6
    return 0

score = 0
for oponent, challenger in input_data:
    if challenger == 'X':
        score += 1
    if challenger == 'Y':
        score += 2
    if challenger == 'Z':
        score += 3
    score += get_win_draw_score(oponent, challenger)
    print(f"round: score: {score}")


    
print(f"score: {score}")














# Try this for submitting...
from aocd import submit
submit(score, part="a", day=2, year=2022)
