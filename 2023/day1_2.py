import re
#!/usr/bin/env python3
"""
Solution for Advent of Code: Day 1 - Trebuchet - Part 1
"""

lookup = ['one', 'two', 'three', 'four', 'five', 'six', \
            'seven', 'eight', 'nine']



def main():
    total = 0
    with open("day1_input_1.txt", "r") as infile:
        for line in infile:
            for ix, letter in enumerate(line):
                if letter.isdigit() or letter[ix:ix+3] in lookup or \
                    letter[ix: ix+4] in lookup or \
            # find the digits in the string
            matches = re.findall(r'\d', line)
            value = int(matches[0]) * 10 + int(matches[-1])

            total = total + value

    print(total)


if __name__ == "__main__":
    main()
