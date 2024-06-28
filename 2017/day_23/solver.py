

import collections


def parse_input():
    with open("input.txt") as f:
        instructions = f.read().splitlines()
    return instructions


def get_value(val_str, registers):
    try:
        val = int(val_str)
    except ValueError:
        val = registers[val_str]
    return val


def execute_p1(instructions, registers, debug=False):
    instr_count = collections.defaultdict(lambda: 0)
    idx = 0
    while 0 <= idx < len(instructions):
        instr = instructions[idx]
        idx += 1
        instr_prefix, values = instr.split(maxsplit=1)
        instr_count[instr_prefix] += 1

        val1_str, val2_str = values.split()
        val1 = get_value(val1_str, registers)
        val2 = get_value(val2_str, registers)
        if instr_prefix == "set":
            registers[val1_str] = val2
            if debug and val1_str == "h":
                print(val1)
        elif instr_prefix == "add":
            registers[val1_str] += val2
            if debug and val1_str == "h":
                print(val1)
        elif instr_prefix == "sub":
            registers[val1_str] -= val2
            if debug and val1_str == "h":
                print(val1)
        elif instr_prefix == "mul":
            registers[val1_str] *= val2
            if debug and val1_str == "h":
                print(val1)
        elif instr_prefix == "mod":
            registers[val1_str] %= val2
        elif instr_prefix == "jnz":
            if val1 != 0:
                idx += val2 - 1
        elif instr_prefix == "jgz":
            if val1 > 0:
                idx += val2 - 1
        else:
            raise ValueError(f"Unknown instruction: {instr_prefix}")

    return instr_count


instructions = parse_input()


# ######## PART 1
registers = collections.defaultdict(lambda: 0)
instr_count = execute_p1(instructions, registers)
print("Part 1 solution: ", instr_count["mul"])

# ######## PART 2
registers = collections.defaultdict(lambda: 0)
registers["a"] = 1
gen_1_counter = execute_p1(instructions, registers)
print("Part 2 solution: ", gen_1_counter)


if __name__ == "__main__":
    pass