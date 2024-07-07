

from collections import Counter


def parse_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


def solve_pt1(ids):
    l2_cnt = 0
    l3_cnt = 0
    for id in ids:
        counts = list(Counter(id).values())
        if 2 in counts:
            l2_cnt += 1
        if 3 in counts:
            l3_cnt += 1
    return l2_cnt * l3_cnt


def solve_pt2(ids):
    id_len = len(ids[0])
    for idx in range(id_len):
        new_ids = [id[:idx] + id[idx+1:] for id in ids]
        (res, cnt), = Counter(new_ids).most_common(1)
        if cnt == 2:
            return res


ids = parse_input()


# ######## PART 1
score = solve_pt1(ids)
print("Part 1 solution: ", score)


# ######## PART 2
pt2_sol = solve_pt2(ids)
print("Part 2 solution: ", pt2_sol)


if __name__ == "__main__":
    pass