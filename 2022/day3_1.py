#!/usr/bin/env python3

import sys
import time

total_priority = 0
for line in sys.stdin:
    items = line.strip()
    count = len(items)
    mid_index = int(count / 2)
    comp1 = items[0:mid_index]
    comp2 = items[mid_index:]

    start = time.time()
    # to find the element that occurs in both
    for item_type in comp1:
        if item_type in comp2:
            item_type_in_both = item_type
            break
    if item_type_in_both.islower():
        priority = ord(item_type_in_both) - ord('a') + 1
    else:
        priority = ord(item_type_in_both) - ord('A') + 27

    total_priority += priority

end = time.time()
print('Sum of all priorities = {}'.format(total_priority))
print('Time taken = {}'.format(end - start))

# runtime = 2.6226043701171875e-0
