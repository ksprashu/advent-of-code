#!/usr/bin/env python3

import sys
import time

def process_3_sacks(sacks):
    sack1, sack2, sack3 = sacks
    for item_type in sack1:
        if item_type in sack2:
            if item_type in sack3:
                item_type_in_both = item_type    
                break
    if item_type_in_both.islower():
        priority = ord(item_type_in_both) - ord('a') + 1
    else:
        priority = ord(item_type_in_both) - ord('A') + 27

    return priority

total_priority = 0
start = time.time()

line_count = 0
sacks = []
for line in sys.stdin:
    sack = line.strip()
    sacks.append(sack)
    line_count += 1
    if line_count == 3:
        line_count = 0
        total_priority += process_3_sacks(sacks)
        sacks = []       

end = time.time()
print('Sum of all priorities = {}'.format(total_priority))
print('Time taken = {}'.format(end - start))

# runtime = 2.6226043701171875e-0

