
from collections import Counter


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    return input_txt


input_txt = parse_input()

# part 1
counter = Counter(list(input_txt))
print("Part 1:", counter["("] - counter[")"])

# part 2
floor = 0
for c_idx, c in enumerate(input_txt, 1):
    floor += 1 if c == "(" else -1
    if floor == -1:
        print("Part 2:", c_idx)
        break

if __name__ == "__main__":
    pass
