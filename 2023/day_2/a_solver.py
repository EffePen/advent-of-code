
import re
import random
import itertools
import collections
from functools import reduce # Valid in Python 2.6+, required in Python 3
import operator


with open('a_input.txt') as f:
    input_txt = f.read()

# ############# part A
color_limit = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

ok_idxs = []
products = []
for l in input_txt.splitlines():
    game_idx_raw, game_raw = l.split(": ")
    game_idx = int(game_idx_raw.split()[1])
    color_dict = collections.defaultdict(lambda: 0)

    for extraction in game_raw.split(";"):
        for cube_ext in extraction.strip().split(","):
            color_num, color = cube_ext.strip().split()
            color_dict[color] = max(int(color_num), color_dict[color])

    if all([color_limit[c] >= color_dict[c] for c in color_limit]):
        ok_idxs.append(game_idx)

    values = list(color_dict.values())
    if min(values) == 0:
        p = 0
    else:
        p = reduce(operator.mul, values, 1)
    products.append(p)

print(sum(ok_idxs))
print(sum(products))

if __name__ == "__main__":
    pass