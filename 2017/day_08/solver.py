
import re
from collections import defaultdict


def parse_input():
    with open("input.txt") as f:
        instructions = f.read().splitlines()
    return instructions


def execute(instructions):
    max_hst_value = 0
    registers = defaultdict(lambda: 0)
    for instr in instructions:
        (reg, op, delta, cond), = re.findall(r"(.+) (.+) (.+) if (.+)", instr)
        cond_reg = cond.split()[0]
        cond = cond.replace(cond_reg, f'registers["{cond_reg}"]')
        if eval(cond):
            registers[reg] += (+1 if op == "inc" else -1) * int(delta)
            max_hst_value = max(max_hst_value, registers[reg])

    return max(registers.values()), max_hst_value


instructions = parse_input()

# ######## PART 1 & 2
sol1, sol2 = execute(instructions)
print("Part 1 solution: ", sol1)
print("Part 2 solution: ", sol2)


if __name__ == "__main__":
    pass