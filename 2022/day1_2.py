#!/usr/bin/env python3

import sys

n_elf = 0
total_cal = 0
largest_cal = 0
largest_elf = 0
n_lines = 0

elf_map = {}

for line in sys.stdin:
    value = line.strip()
    if len(value) > 0:
        total_cal += int(value)
    else:
        elf_map[n_elf] = total_cal
        total_cal = 0
        n_elf += 1

cal_carried = sorted(list(elf_map.values()), reverse=True)
top3_cals = cal_carried[0] + cal_carried[1] + cal_carried[2]

print(top3_cals)
