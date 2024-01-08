
import re

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    strings = input_txt.splitlines()
    return strings

strings = parse_input()

# part 1
cnt_nice = 0
forbidden_subs = ["ab", "cd", "pq", "xy"]
for s in strings:
    if not any(fs in s for fs in forbidden_subs):
        if any(s[idx] == s[idx+1] for idx in range(len(s) - 1)):
            if len(s) - len(re.sub("[aeiou]", "", s)) >= 3:
                cnt_nice += 1

print("Part 1:", cnt_nice)

# part 2
cnt_nice = 0
for s in strings:
    same_nonoverlapping_pair = False
    for idx1 in range(len(s) - 1):
        for idx2 in range(idx1 + 2, len(s) - 1):
            if s[idx1:idx1+2] == s[idx2:idx2+2]:
                same_nonoverlapping_pair = True

    same_side_chars = False
    for idx1 in range(1, len(s) - 1):
        if s[idx1-1] == s[idx1+1]:
            same_side_chars = True
            break

    if same_side_chars and same_nonoverlapping_pair:
        cnt_nice += 1

print("Part 2:", cnt_nice)


if __name__ == "__main__":
    pass
