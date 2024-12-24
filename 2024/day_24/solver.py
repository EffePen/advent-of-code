

import re


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    initialization_txt, gates_txt = input_txt.split("\n\n")
    values = {e.split(": ")[0]: int(e.split(": ")[1]) for e in initialization_txt.splitlines()}
    gates = []
    for gate_txt in gates_txt.splitlines():
        (e1, operator, e2, out), = re.findall(r"(.+) (.+) (.+) -> (.+)", gate_txt)
        gates.append(((e1, e2), operator, out))

    return values, gates


def solve_pt1(values, gates):
    while gates:
        remove_idxs = []
        for idx, (operands, operator, out) in enumerate(gates):
            if all(op in values for op in operands):
                if operator == "AND":
                    v = values[operands[0]] & values[operands[1]]
                elif operator == "OR":
                    v = values[operands[0]] | values[operands[1]]
                elif operator == "XOR":
                    v = values[operands[0]] ^ values[operands[1]]
                else:
                    raise ValueError
                values[out] = v
                remove_idxs.append(idx)

        for idx in remove_idxs[::-1]:
            del gates[idx]

    score = 0
    for idx, (k, v) in enumerate(sorted([(k, v) for k, v in values.items() if k.startswith("z")], key=lambda x: x[0])):
        score += (v << idx)

    return score


def solve_pt2(values, gates):
    score = 0
    return score


# PARSE INPUT
values, gates = parse_input()

# PART 1
score = solve_pt1(values, gates)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(values, gates)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass