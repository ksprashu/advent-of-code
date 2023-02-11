#!/usr/bin/env python3

import sys

n_elf = 1
total_cal = 0
largest_cal = 0
largest_elf = 0
n_lines = 0

for line in sys.stdin:
    value = line.strip()
    if len(value) > 0:
        total_cal += int(value)
    else:
        if total_cal > largest_cal:
            largest_cal = total_cal
            largest_elf = n_elf
        total_cal = 0
        n_elf += 1

print("Elf {} is carrying {} calories".format(largest_elf, largest_cal))
