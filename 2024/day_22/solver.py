

from collections import defaultdict


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
    scores = {}
    solution = defaultdict(int)
    for s_idx, secret in enumerate(initial_nums):
        seq = [secret % 10]
        diffs = []
        scores[s_idx] = dict()
        for idx in range(2000):
            secret = ((secret * 64) ^ secret) % 16777216
            secret = ((int(secret // 32)) ^ secret) % 16777216
            secret = ((secret * 2048) ^ secret) % 16777216
            seq.append(secret % 10)
            diffs.append(seq[-1] - seq[-2])
            if len(diffs) >= 4:
                key = tuple(diffs[-4:])
                if key not in scores[s_idx]:
                    scores[s_idx][key] = seq[-1]
                    solution[key] += seq[-1]

    return max(solution.values())


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