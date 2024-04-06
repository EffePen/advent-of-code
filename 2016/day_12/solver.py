
def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    instructions = input_txt.splitlines()
    return instructions


def get_register_or_int(val, registers):
    if val in registers:
        val = registers[val]
    else:
        val = int(val)
    return val


def apply_instruction(idx, registers, instructions):
    instr = instructions[idx]
    instr_type, instr_args_txt = instr.split(" ", 1)
    instr_args = instr_args_txt.split()

    idx += 1
    if instr_type == 'cpy':
        val, reg_id = instr_args
        val = get_register_or_int(val, registers)
        registers[reg_id] = val
    elif instr_type == 'inc':
        reg_id, = instr_args
        registers[reg_id] += 1
    elif instr_type == 'dec':
        reg_id, = instr_args
        registers[reg_id] -= 1
    elif instr_type == 'jnz':
        val, jump_len = instr_args
        val = get_register_or_int(val, registers)
        jump_len = get_register_or_int(jump_len, registers)
        if val != 0:
            idx += int(jump_len) - 1
    return idx, registers


# PART 1
registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
instructions = parse_input()
toggled = [False for _ in instructions]

idx = 0
while idx < len(instructions):
    idx, registers = apply_instruction(idx, registers=registers, instructions=instructions)
print(f"Part 1 solution: {registers['a']}")


# PART 2
registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

idx = 0
while idx < len(instructions):
    idx, registers = apply_instruction(idx, registers, instructions)
print(f"Part 2 solution: {registers['a']}")


if __name__ == "__main__":
    pass