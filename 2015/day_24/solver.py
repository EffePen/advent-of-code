
import math
import itertools


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    weights = [int(e) for e in input_txt.splitlines()]
    return weights


def solve(weights, num_groups):
    assert len(weights) == len(set(weights))
    tot_weight = sum(weights)
    group_weight = tot_weight / num_groups

    for num_elements in range(1, len(weights) + 1):
        try:
            entanglement = min(math.prod(c) for c in itertools.combinations(weights, num_elements) if sum(c) == group_weight)
            return entanglement
        except ValueError:
            continue


# input
weights = parse_input()

# part 1
score = solve(weights, num_groups=3)
print("Part 1:", score)

# part 2
score = solve(weights, num_groups=4)
print("Part 2:", score)


if __name__ == "__main__":
    pass
