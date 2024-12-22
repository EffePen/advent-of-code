

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    initial_nums = [int(n) for n in input_txt.splitlines()]
    return initial_nums


def solve_pt1(initial_nums):
    score = 0
    for secret in initial_nums:
        for _ in range(2000):
            secret = ((secret * 64) ^ secret) % 16777216
            secret = ((int(secret // 32)) ^ secret) % 16777216
            secret = ((secret * 2048) ^ secret) % 16777216
        score += secret
    return score


def solve_pt2(initial_nums):
    score = 0
    return score


# PARSE INPUT
initial_nums = parse_input()

# PART 1
score = solve_pt1(initial_nums)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(initial_nums)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass