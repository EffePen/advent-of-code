
import re
import random
import itertools
import collections
from functools import reduce # Valid in Python 2.6+, required in Python 3
import operator


with open('a_input.txt') as f:
    input_txt = f.read()

part_numbers = []
gears = dict()

lines = input_txt.splitlines()
for l_idx, curr_l in enumerate(lines):
    matrix_size = len(curr_l)

    # Get previous and succ lines
    if l_idx == 0:
        prev_l = "." * len(curr_l)
        succ_l = lines[l_idx+1]
    elif l_idx == len(lines) -1:
        prev_l = lines[l_idx-1]
        succ_l = "." * len(curr_l)
    else:
        prev_l = lines[l_idx-1]
        succ_l = lines[l_idx + 1]

    # Find all numbers in current line and check symbols around
    for num_match in re.finditer("[0-9]+", curr_l):
        num = curr_l[num_match.start():num_match.end()]
        min_idx = max(0, num_match.start()-1)
        max_idx = min(matrix_size, num_match.end()+1)
        upper_substr = prev_l[min_idx:max_idx]
        lower_substr = succ_l[min_idx:max_idx]
        l_char = curr_l[num_match.start()-1] if num_match.start() != 0 else '.'
        r_char = curr_l[num_match.end()] if num_match.end() != matrix_size else '.'

        neigh_chars = re.sub(r"\.", "", upper_substr + lower_substr + l_char + r_char)
        if neigh_chars:
            part_numbers.append(int(num))
            curr_num_gears_coords = []
            # check gears in prev line
            for gear_match in re.finditer("\*", upper_substr):
                curr_num_gears_coords.append((l_idx-1, min_idx + gear_match.start()))

            # check gears in succ line
            for gear_match in re.finditer("\*", lower_substr):
                curr_num_gears_coords.append((l_idx+1, min_idx + gear_match.start()))

            # check gears in l and r char
            if l_char == "*":
                curr_num_gears_coords.append((l_idx, num_match.start()-1))

            if r_char == "*":
                curr_num_gears_coords.append((l_idx, num_match.end()))

            for gear_coords in curr_num_gears_coords:
                if not gears.get(gear_coords):
                    gears[gear_coords] = []
                gears[gear_coords].append(int(num))

print(sum(part_numbers))
print(sum([vals[0]*vals[1] for vals in gears.values() if len(vals) == 2]))

if __name__ == "__main__":
    pass
