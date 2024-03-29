

from collections import Counter


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    codes = input_txt.splitlines()
    return codes


# PARSE INPUT
codes = parse_input()

# PART 1
letter_columns = list(zip(*codes))
part1_code = "".join([Counter(letter_column).most_common()[0][0][0] for letter_column in letter_columns])
print(f"Part 1 solution: {part1_code}")

# PART 2
part2_code = "".join([Counter(letter_column).most_common()[-1][0][0] for letter_column in letter_columns])
print(f"Part 2 solution: {part2_code}")

if __name__ == "__main__":
    pass