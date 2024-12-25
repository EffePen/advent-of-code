

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()

    keys = {}
    locks = {}
    for idx, inp in enumerate(input_txt.split("\n\n")):
        heigths = [l.count("#") for l in zip(*inp.splitlines())]
        if inp.startswith("#####"):
            locks[idx] = heigths
        else:
            keys[idx] = heigths

    return keys, locks


def solve(keys, locks):
    score = 0
    for k_idx, k in keys.items():
        for l_idx, l in locks.items():
            score += all(e1 + e2 <= 7 for e1, e2 in zip(k, l))

    return score


# PARSE INPUT
keys, locks = parse_input()

# PART 1 & 2
score = solve(keys, locks)
print(f"Solution: {score}")


if __name__ == "__main__":
    pass
