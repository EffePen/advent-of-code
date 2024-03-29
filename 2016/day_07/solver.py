import itertools
import re

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    codes = input_txt.splitlines()
    return codes


def has_abba(subcode):
    res = any([(subcode[idx] != subcode[idx+1]) and (subcode[idx:idx+2] == subcode[idx+2:idx+4][::-1])
                for idx in range(len(subcode)-3)])
    return res


def get_aba_codes(subcode):
    res = [subcode[idx:idx+3] for idx in range(len(subcode)-2)
           if (subcode[idx] != subcode[idx+1]) and (subcode[idx] == subcode[idx+2])]
    return res


def has_abba(subcode):
    res = any([(subcode[idx] != subcode[idx+1]) and (subcode[idx:idx+2] == subcode[idx+2:idx+4][::-1])
                for idx in range(len(subcode)-3)])
    return res

# PARSE INPUT
codes = parse_input()

# PART 1
part1_score = 0
part2_score = 0
for code in codes:
    supernet_parts = re.split(r"\[[^\[\]]*\]", code)
    hypernet_parts = re.findall(r"\[([^\[\]]*)\]", code)

    # PART 1
    is_ok1 = any([has_abba(subcode) for subcode in supernet_parts])
    is_ko1 = any([has_abba(subcode) for subcode in hypernet_parts])

    if is_ok1 and not is_ko1:
        part1_score += 1

    # PART 2
    aba_codes = list(itertools.chain.from_iterable([get_aba_codes(subcode) for subcode in supernet_parts]))
    bab_codes = [c[1] + c[0] + c[1] for c in aba_codes]
    is_ok2 = any([any([bab_code in subcode for subcode in hypernet_parts]) for bab_code in bab_codes])

    if is_ok2:
        part2_score += 1

print(f"Part 1 solution: {part1_score}")
print(f"Part 2 solution: {part2_score}")


if __name__ == "__main__":
    pass