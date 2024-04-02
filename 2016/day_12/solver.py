import re


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    instructions = input_txt.splitlines()
    return instructions

# PART 1
registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
instructions = parse_input()

idx = 0
while idx < len(instructions):
    instr = instructions[idx]
    idx += 1
    if instr.startswith('cpy'):
        (val, reg_id), = re.findall(r"cpy (.+) (.+)", instr)
        if val in registers:
            registers[reg_id] = registers[val]
        else:
            registers[reg_id] = int(val)
    elif instr.startswith('inc'):
        (reg_id), = re.findall(r"inc (.+)", instr)
        registers[reg_id] += 1
    elif instr.startswith('dec'):
        (reg_id), = re.findall(r"dec (.+)", instr)
        registers[reg_id] -= 1
    elif instr.startswith('inc'):
        (reg_id), = re.findall(r"inc (.+)", instr)
        registers[reg_id] += 1
    elif instr.startswith('jnz'):
        (val, jump_len), = re.findall(r"jnz (.*) (.*)", instr)
        try:
            val = int(val)
        except:
            val = registers[val]
        if val != 0:
            idx += int(jump_len) - 1

print(f"Part 1 solution: {registers['a']}")


# PART 2
registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
instructions = parse_input()

idx = 0
while idx < len(instructions):
    instr = instructions[idx]
    idx += 1
    if instr.startswith('cpy'):
        (val, reg_id), = re.findall(r"cpy (.+) (.+)", instr)
        if val in registers:
            registers[reg_id] = registers[val]
        else:
            registers[reg_id] = int(val)
    elif instr.startswith('inc'):
        (reg_id), = re.findall(r"inc (.+)", instr)
        registers[reg_id] += 1
    elif instr.startswith('dec'):
        (reg_id), = re.findall(r"dec (.+)", instr)
        registers[reg_id] -= 1
    elif instr.startswith('jnz'):
        (val, jump_len), = re.findall(r"jnz (.*) (.*)", instr)
        try:
            val = int(val)
        except:
            val = registers[val]
        if val != 0:
            idx += int(jump_len) - 1

print(f"Part 2 solution: {registers['a']}")


#print(f"Part 1 solution: {part2_solution}")

if __name__ == "__main__":
    pass