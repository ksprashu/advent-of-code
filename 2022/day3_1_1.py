#!/usr/bin/env python3

# Attempt to optimize with sets

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
    set1 = {x for x in comp1}
    set2 = {x for x in comp2}
    # item_type_in_both = list(set1.intersection(set2))[0]
    for item_type in set1:
        if item_type in set2:
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

# runtime = 3.814697265625e-06

