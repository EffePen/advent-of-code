

import re


def parse_input():
    with open("input.txt") as f:
        polymer = f.read()
    return polymer


def collapse(polymer):
    patterns = []
    patterns += [f"{ll}{ll.upper()}" for ll in set(polymer.lower())]
    patterns += [f"{ll.upper()}{ll}" for ll in set(polymer.lower())]
    union_pattern = "|".join(patterns)

    prev_len = None
    while len(polymer) != prev_len:
        prev_len = len(polymer)
        polymer = re.sub(union_pattern, "", polymer)
    return polymer


def optimize(polymer):
    polymer = collapse(polymer)
    molecule_score = {}
    for molecule in sorted(set(polymer.lower())):
        # pattern = f"{molecule}|{molecule.upper()}"
        # new_polymer = re.sub(pattern, "", polymer)
        new_polymer = polymer.replace(molecule, "").replace(molecule.upper(), "")
        molecule_score[molecule] = len(collapse(new_polymer))
    return min(molecule_score.values())


polymer = parse_input()


# ######## PART 1
new_polymer = collapse(polymer)
print("Part 1 solution: ", len(new_polymer))


## ######## PART 2
score = optimize(polymer)
print("Part 2 solution: ", score)


if __name__ == "__main__":
    pass