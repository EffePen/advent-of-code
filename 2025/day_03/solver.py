

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    banks = input_txt.splitlines()
    return banks


def solve_pt1(banks):
    score = 0
    for bank in banks:
        first_digit = max(list(bank[:-1]))
        first_idx = bank.find(first_digit)
        second_digit = max(list(bank[first_idx+1:]))
        jolt = int(first_digit + second_digit)
        score += jolt

    return score


def solve_pt2(banks):
    score = 0
    for bank in banks:
        digits = []
        num_digits = 12
        last_idx = 0
        for d_idx in range(1, num_digits+1):
            bank_subset = bank[last_idx:-num_digits+d_idx if -num_digits+d_idx != 0 else None]
            digit = max(list(bank_subset))
            last_idx = bank_subset.find(digit) + last_idx + 1
            digits.append(digit)
        jolt = int("".join(digits))
        score += jolt
    return score


# PARSE INPUT
banks = parse_input()

# PART 1
score = solve_pt1(banks)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(banks)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass