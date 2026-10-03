import re
#!/usr/bin/env python3
"""
Solution for Advent of Code: Day 1 - Trebuchet - Part 1
"""


def main():
    total = 0
    with open("day1_input_1_100.txt", "r") as infile:
        for line in infile:
            # find the digits in the string
            matches = re.findall(r'\d', line)
            value = int(matches[0]) * 10 + int(matches[-1])

            total = total + value

    print(total)


if __name__ == "__main__":
    main()
