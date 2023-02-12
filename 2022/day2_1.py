#!/usr/bin/env python3

import sys

# Sample Input
# Col 1 - opponent play (A Rock, B Paper, C Scissors)
# Col 2 - ?? (X Rock, Y Paper, Z Scissors)
# Scores - Rock = 1, Paper = 2, Scissors = 3
# Scores - Lost = 0, Draw = 3, Won = 6

choice_values = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}
round_value = {'won': 6, 'draw': 3, 'lose': 0}

total_score = 0
round_status = ''

for line in sys.stdin:
    play1, play2 = line.split()

    if choice_values.get(play2) == choice_values.get(play1):
        round_status = 'draw'
    elif play2 == 'X' and play1 == 'C':
        round_status = 'won'
    elif play2 == 'Z' and play1 == 'A':
        round_status = 'lose'
    elif (choice_values.get(play2) > choice_values.get(play1)):
        round_status = 'won'
    else:
        round_status = 'lose'

    total_score += choice_values.get(play2)
    total_score += round_value.get(round_status)
    
    print('Played = {}-{}, Status = {}, Score = {}+{}, Total = {}'.format(play1, play2, 
        round_status, choice_values.get(play2), round_value.get(round_status), total_score))

print('final score = {}'.format(total_score))
