import re

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    codes = input_txt.splitlines()
    return codes


# PART 1
codes = parse_input()
new_codes = []

for code in codes:
    new_code_parts = []
    while True:
        match = re.search("\(\d*x\d*\)", code)
        if match:
            # substr preceding tag
            new_code_parts.append(code[:match.span()[0]])

            # repeated substr
            length, repeat = map(int, match.group(0)[1:-1].split("x"))
            substr_start = match.span()[1]
            new_code_parts.append(code[substr_start:substr_start+length] * repeat)
            code = code[substr_start+length:]
        else:
            new_code_parts.append(code)
            break

    new_code = "".join(new_code_parts)
    new_codes.append(new_code)

print(f"Part 1 solution: {sum([len(code) for code in new_codes])}")

# PART 2
codes = parse_input()
new_codes_length = []


def calculate_len(code):
    cumulative_len = 0
    match = re.search(r"\(\d+x\d+\)", code)
    if match:

        # split code
        length, repeat = map(int, match.group(0)[1:-1].split("x"))
        repeat_start = match.span()[1]

        prec_code = code[:match.span()[0]]
        succ_code = code[repeat_start + length:]
        repeated_code = code[repeat_start:repeat_start + length]

        # substr preceding tag
        cumulative_len += len(prec_code)
        cumulative_len += calculate_len(repeated_code) * repeat
        cumulative_len += calculate_len(succ_code)
        return cumulative_len
    else:
        cumulative_len += len(code)
        return cumulative_len


for code in codes:
    code_len = calculate_len(code)
    new_codes_length.append(code_len)

print(f"Part 2 solution: {sum(new_codes_length)}")

if __name__ == "__main__":
    pass