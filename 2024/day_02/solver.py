

from collections import Counter


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    reports = [[int(e) for e in l.split()] for l in input_txt.splitlines()]
    return reports


def is_safe(r):
    status_list = []
    for idx in range(len(r) - 1):
        if 1 <= abs(r[idx] - r[idx + 1]) <= 3:
            if r[idx] < r[idx + 1]:
                # increasing
                status_list.append(+1)
            else:
                # decreasing
                status_list.append(-1)
        else:
            # neither "increasing" nor "decreasing" according to the roles
            status_list.append(0)

    # only a single status type is present, and is not 0
    return len(set(status_list)) == 1 and list(set(status_list))[0] != 0


def solve_pt1(reports):
    score = 0
    for r in reports:
        if is_safe(r):
            score += 1
    return score


def solve_pt2(reports):
    score = 0
    for r in reports:
        if is_safe(r):
            # check if it is safe as it is
            score += 1
        else:
            # check if it would be safe removing a single element
            for idx in range(len(r)):
                if is_safe(r[:idx] + r[idx+1:]):
                    score += 1
                    break
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