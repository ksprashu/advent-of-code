#!/usr/bin/env python3
# To find fully encompassed sections between the elves

import sys

def read_input_line():
    line = sys.stdin.readline()
    if not line:
        raise EOFError
    return line.strip().split(',')


def get_range_as_list(in_range):
    start, end = in_range.split('-')
    return [x for x in range(int(start), int(end) + 1)]


def are_sections_contained(section1, section2):
    # ensure section1 starts smaller and is also the larger list
    if section1[0] > section2[0]:
        section1, section2 = section2, section1
    if section1[0] == section2[0] and len(section1) < len(section2):
        section1, section2 = section2, section1

    if section2[0] <= section1[-1]:
        return True
    
    return False
    

def main():
    print("Starting program")
    no_more_input = False
    contained_sections_count = 0
    while not no_more_input:
        try:
            range1, range2 = read_input_line()
            sections1 = get_range_as_list(range1)
            sections2 = get_range_as_list(range2)
            if are_sections_contained(sections1, sections2):
                contained_sections_count += 1
        except EOFError:
            print("End of input")
            no_more_input = True

    print("{} ranges overlap".format(contained_sections_count))    


if __name__ == "__main__":
    # test read input
    # print(read_input_line())
    # print(get_range_as_list(read_input_line()[0]))
    main()