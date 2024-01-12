

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    sues = dict()
    for line_txt in input_txt.splitlines():
        sue_id, vals_txt = line_txt.split(": ", maxsplit=1)
        sues[sue_id] = {e.split()[0][:-1]: int(e.split()[1]) for e in vals_txt.split(", ")}
    return sues


def part1(sues):
    for sue_id, sue_vals in sues.items():
        if all(sue_vals[k] == REFERENCE_SUE_VALS.get(k) for k in sue_vals):
            return sue_id


def p2_compare(k, sue_vals):
    if k in ("cats", "trees"):
        return sue_vals[k] > REFERENCE_SUE_VALS.get(k)
    elif k in ("pomeranians", "goldfish"):
        return sue_vals[k] < REFERENCE_SUE_VALS.get(k)
    else:
        return REFERENCE_SUE_VALS.get(k) == sue_vals[k]


def part2(sues):
    for sue_id, sue_vals in sues.items():
        if all(p2_compare(k, sue_vals) for k in sue_vals):
            return sue_id


REFERENCE_SUE_VALS = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


# input
sues = parse_input()

# part 1
sue_id = part1(sues)
print("Part 1:", sue_id)

# part 2
sue_id = part2(sues)
print("Part 2:", sue_id)


if __name__ == "__main__":
    pass
