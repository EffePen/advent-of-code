
from itertools import groupby

input_txt = "1321131112"

# part 1 & 2
code = [int(e) for e in input_txt]
for idx in range(1, 51):
    new_code = []
    for k, group in groupby(code):
        new_code.extend([len(list(group)), k])
    code = new_code
    if idx == 40:
        print("Part 1:", len(code))
    elif idx == 50:
        print("Part 2:", len(code))

if __name__ == "__main__":
    pass
