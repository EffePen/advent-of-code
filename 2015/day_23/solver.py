

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    instructions = input_txt.splitlines()
    return instructions


def part12(instructions, registers):
    idx = 0

    while 0 <= idx < len(instructions):
        instr, instr_add_info = instructions[idx].split(maxsplit=1)
        d_idx = 1

        if instr == "jmp":
            d_idx = int(instr_add_info)
        elif instr in ("jio", "jie"):
            rid, jval_str = instr_add_info.split(", ")
            if instr == "jio" and registers[rid] == 1:
                d_idx = int(jval_str)
            if instr == "jie" and registers[rid] % 2 == 0:
                d_idx = int(jval_str)
        else:
            rid = instr_add_info
            if instr == "inc":
                registers[rid] += 1
            elif instr == "tpl":
                registers[rid] *= 3
            elif instr == "hlf":
                registers[rid] /= 2
            else:
                raise ValueError

        idx += d_idx

    return registers


# input
instructions = parse_input()

# part 1
registers = part12(instructions, registers={"a": 0, "b": 0})
print("Part 1:", registers["b"])

# part 2
registers = part12(instructions, registers={"a": 1, "b": 0})
print("Part 2:", registers["b"])

if __name__ == "__main__":
    pass
