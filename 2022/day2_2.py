#!/usr/bin/env python3

import sys

# Sample Input
# Col 1 - opponent play (A Rock, B Paper, C Scissors)
# Col 2 - your play (X lose, Y draw, Z win)
# Scores - Rock = 1, Paper = 2, Scissors = 3
# Scores - Lost = 0, Draw = 3, Won = 6

choice_values = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}
round_value = {'won': 6, 'draw': 3, 'lose': 0}
round_result = {'X': 'lose', 'Y': 'draw', 'Z': 'won'}

total_score = 0
round_status = ''
round_score = 0

for line in sys.stdin:
    play1, play2 = line.split()

    round_status = round_result.get(play2)
    if round_status == 'draw':
        round_score = choice_values.get(play1)
    elif round_status == 'won':
        round_score = choice_values.get(play1) + 1 if play1 != 'C' else 1
    else:
        round_score = choice_values.get(play1) - 1 if play1 !='A' else 3

    total_score += round_score
    total_score += round_value.get(round_status)
    
    print('Played = {}-{}, Status = {}, Score = {}+{}, Total = {}'.format(play1, play2, 
        round_status, round_score, round_value.get(round_status), total_score))

print('final score = {}'.format(total_score))
