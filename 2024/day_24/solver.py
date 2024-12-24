

import re


def parse_input(mod=False):
    with open("input.txt" if not mod else "input_mod.txt") as f:
        input_txt = f.read()
    initialization_txt, gates_txt = input_txt.split("\n\n")
    values = {e.split(": ")[0]: int(e.split(": ")[1]) for e in initialization_txt.splitlines()}
    gates = []
    for gate_txt in gates_txt.splitlines():
        (e1, operator, e2, out), = re.findall(r"(.+) (.+) (.+) -> (.+)", gate_txt)
        gates.append((tuple(sorted((e1, e2))), operator, out))

    return values, gates


def solve_pt1(values, gates):
    gates = gates.copy()
    values = values.copy()
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


def solve_pt2(mod_gates, original_gates):
    gates_dict = {(g[0], g[1]): g[2] for g in mod_gates}
    original_gates_dict = {(g[0], g[1]): g[2] for g in original_gates}

    # NOTE: the following cycle checks that the operations for the binary adder give the expected output
    # => run the debugger and fix the assertion errors by switching output pairs
    # then inspect manually the outputs that have changed, sort and print them
    carry_out = None
    for idx in range(45):
        a_in = f"x{str(idx).zfill(2)}"
        b_in = f"y{str(idx).zfill(2)}"
        carry_in = carry_out

        if carry_in is None:
            s = gates_dict[((a_in, b_in), "XOR")]
            carry_out = gates_dict[((a_in, b_in), "AND")]
            assert s == f"z{str(idx).zfill(2)}"
        else:
            s1 = gates_dict[((a_in, b_in), "XOR")]
            s = gates_dict.get(((carry_in, s1), "XOR")) or gates_dict.get(((s1, carry_in), "XOR"))
            assert s == f"z{str(idx).zfill(2)}"

            carry_out_1 = gates_dict.get(((a_in, b_in), "AND")) or gates_dict.get(((b_in, a_in), "AND"))
            carry_out_2 = gates_dict.get(((s1, carry_in), "AND")) or gates_dict.get(((carry_in, s1), "AND"))
            carry_out = gates_dict.get(((carry_out_2, carry_out_1), "OR")) or gates_dict.get(((carry_out_1, carry_out_2), "OR"))

    mod_outputs = [v for k, v in original_gates_dict.items() if v != gates_dict[k]]

    return ",".join(sorted(mod_outputs))


# PART 1
values, gates = parse_input(mod=False)
score = solve_pt1(values, gates)
print(f"Part 1 solution: {score}")


# PART 2
values, mod_gates = parse_input(mod=True)
score = solve_pt2(mod_gates, original_gates=gates)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass