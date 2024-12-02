

from collections import Counter


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    pairs = [[int(e) for e in l.split()] for l in input_txt.splitlines()]
    return pairs


def solve_pt1(pairs):
    l1, l2 = zip(*pairs)
    sorted_l1 = sorted(l1)
    sorted_l2 = sorted(l2)
    score = 0
    for e1, e2 in zip(sorted_l1, sorted_l2):
        score += abs(e1 - e2)
    return score


def solve_pt2(pairs):
    l1, l2 = zip(*pairs)
    l2_counter = Counter(l2)

    score = 0
    for e in l1:
        score += e * l2_counter[e]
    return score


# PARSE INPUT
pairs = parse_input()

# PART 1
score = solve_pt1(pairs)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(pairs)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass