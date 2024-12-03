

import re


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    return input_txt


def solve_pt1(input_txt):
    score = 0
    # extract multiplication pattern
    pattern = r"mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)"
    multiplications = re.findall(pattern, input_txt)
    for mul in multiplications:
        # extract factors and multiply them together
        n1, n2 = [int(e) for e in mul.strip("mul(").strip(")").split(",")]
        score += n1 * n2
    return score


def solve_pt2(input_txt):
    score = 0
    # extract multiplication, do and don't patterns
    pattern = r"(mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)|do\(\)|don't\(\))"
    multiplications = re.findall(pattern, input_txt)

    # check multiplication enablement and, in case, extract factors and multiply them together
    enabled = True
    for mul in multiplications:
        if mul == "do()":
            enabled = True
        elif mul == "don't()":
            enabled = False
        elif mul.startswith("mul("):
            if enabled:
                n1, n2 = [int(e) for e in mul.strip("mul(").strip(")").split(",")]
                score += n1 * n2
        else:
            raise ValueError
    return score


# PARSE INPUT
input_txt = parse_input()

# PART 1
score = solve_pt1(input_txt)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(input_txt)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass