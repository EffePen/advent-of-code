
from functools import cache


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    towels_str, patterns_str = input_txt.split("\n\n")
    towels = towels_str.split(", ")
    patterns = patterns_str.splitlines()

    return towels, patterns


@cache
def recurse(pattern, towels):
    if pattern == "":
        return 1
    else:
        return sum(recurse(pattern[len(towel):], towels) for towel in towels if pattern.startswith(towel))


def solve(towels, patterns, part):
    score = 0
    for pattern in patterns:
        p_score = recurse(pattern, tuple(towels))
        if p_score > 0:
            score += 1 if part == 1 else p_score
    return score


# PARSE INPUT
towels, patterns = parse_input()

# PART 1
score = solve(towels, patterns, part=1)
print(f"Part 1 solution: {score}")


# PART 2
score = solve(towels, patterns, part=2)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass
