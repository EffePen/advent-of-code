
import re


def parse_input():
    with open("input.txt") as f:
        stream_txt = f.read()
    return stream_txt


def solve_pt12(stream_txt):
    # remove canceled chars
    stream_txt = re.sub(r"!.", "", stream_txt)

    # find and remove garbage
    num_garbage_groups = len(re.findall(r"<[^>]*>", stream_txt))
    stream_len_w_garbage = len(stream_txt)
    stream_txt = re.sub(r"<[^>]*>", "", stream_txt)
    stream_len_wo_garbage = len(stream_txt)

    # note: remove <> for each garbage group
    garbage_size = stream_len_w_garbage - stream_len_wo_garbage - 2*num_garbage_groups

    score = 0
    group_val = 0
    for char in stream_txt:
        if char == "{":
            group_val += 1
        elif char == "}":
            score += group_val
            group_val -= 1

    return score, garbage_size




stream_txt = parse_input()

# ######## PART 1 & 2
score, garbage_size = solve_pt12(stream_txt)
print("Part 1 solution: ", score)
print("Part 2 solution: ", garbage_size)


if __name__ == "__main__":
    pass