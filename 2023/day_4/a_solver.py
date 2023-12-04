
import re
import random
import itertools
import collections
from functools import reduce # Valid in Python 2.6+, required in Python 3
import operator


with open('a_input.txt') as f:
    input_txt = f.read()

lines = input_txt.splitlines()

points = []
card_copies = {}

for l in lines:
    card_id, card_info = l.split(":")
    curr_card_idx = int(card_id.strip().split()[-1])
    if curr_card_idx not in card_copies:
        card_copies[curr_card_idx] = 1 # init

    winning_raw, playing_raw = card_info.split("|")
    winning_numbers = set([int(n) for n in winning_raw.strip().split()])
    playing_numbers = set([int(n) for n in playing_raw.strip().split()])

    matching_numbers = winning_numbers & playing_numbers
    num_matching_numbers = len(matching_numbers)
    points.append(0 if not matching_numbers else 2**(num_matching_numbers-1))

    for copied_idx in range(curr_card_idx + 1, curr_card_idx + 1 + num_matching_numbers):
        if copied_idx not in card_copies:
            card_copies[copied_idx] = 1  # init
        card_copies[copied_idx] += card_copies[curr_card_idx]

print(sum(points))
print(sum(card_copies.values()))

if __name__ == "__main__":
    pass
