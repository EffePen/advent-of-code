

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    instructions = input_txt.splitlines()
    instructions = [instr.split("#")[0].strip() for instr in instructions]
    return instructions


def get_register_or_int(val, registers):
    if val in registers:
        val = registers[val]
    else:
        val = int(val)
    return val


def toggle_instruction(instr):
    instr_type, instr_args_txt = instr.split(" ", 1)
    instr_args = instr_args_txt.split()
    if len(instr_args) == 1:
        if instr_type == "inc":
            instr_type = "dec"
        else:
            instr_type = "inc"
    elif len(instr_args) == 2:
        if instr_type == "jnz":
            instr_type = "cpy"
        else:
            instr_type = "jnz"
    else:
        raise ValueError
    toggled_instr = f"{instr_type} {instr_args_txt}"
    return toggled_instr


def apply_instruction(idx, registers, instructions):
    instr = instructions[idx]
    instr_type, instr_args_txt = instr.split(" ", 1)
    instr_args = instr_args_txt.split()

    idx += 1
    if instr_type == 'tgl':
        jump_len, = instr_args
        jump_len = get_register_or_int(jump_len, registers)
        try:
            toggled_idx = idx - 1 + int(jump_len)
            instr_to_toggle = instructions[toggled_idx]
            instructions[toggled_idx] = toggle_instruction(instr_to_toggle)
        except IndexError:
            pass
    elif instr_type == 'cpy':
        val, reg_id = instr_args
        val = get_register_or_int(val, registers)
        if reg_id in registers:
            registers[reg_id] = val
    elif instr_type == 'inc':
        reg_id, = instr_args
        if reg_id in registers:
            registers[reg_id] += 1
    elif instr_type == 'dec':
        reg_id, = instr_args
        if reg_id in registers:
            registers[reg_id] -= 1
    elif instr_type == 'jnz':
        val, jump_len = instr_args
        val = get_register_or_int(val, registers)
        jump_len = get_register_or_int(jump_len, registers)
        if val != 0:
            idx += int(jump_len) - 1
    return idx, registers


def translated_assembly(a):
    score = a
    for idx in range(a-2):
        score *= (a - 1 - idx)
    score += 88 * 75
    return score


# PART 1
registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
instructions = parse_input()

idx = 0
while idx < len(instructions):
    idx, registers = apply_instruction(idx, registers=registers, instructions=instructions)
score = translated_assembly(a=7)
print(f"Part 1 solution: {registers['a']}")
print(f"Part 1 solution: {score}")


# PART 2
score = translated_assembly(a=12)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass