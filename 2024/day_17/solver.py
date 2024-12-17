

import re


def parse_input(debug=False):
    with open("input.txt") as f:
        input_txt = f.read()
    registers_txt, program_txt = input_txt.split("\n\nProgram: ")
    (a, b, c), = [[int(e) for e in m] for m in re.findall(r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)", registers_txt)]
    registers = {4: a, 5: b, 6: c}
    program = [int(e) for e in program_txt.split(",")]

    if debug:
        # write assembly code to disk for manual inspection
        with open("assembly.txt", "w") as f:
            idx = 0
            operand_map = {4: "a", 5: "b", 6: "c"}
            while 0 <= idx < len(program) - 1:
                opcode, operand = program[idx:idx + 2]
                if opcode == 0:  # adv
                    f.write(f"a = a >> {operand_map.get(operand, operand)}\n")
                elif opcode == 1:  # bxl
                    f.write(f"b = b ^ {operand}\n")
                elif opcode == 2:  # bst
                    f.write(f"b = {operand_map.get(operand, operand)} & 7\n")
                elif opcode == 3:  # jnz
                    f.write(f"if a != 0 then jump to {operand}\n")
                elif opcode == 4:  # bxc
                    f.write(f"b = b ^ c\n")
                elif opcode == 5:  # out
                    f.write(f"out {operand_map.get(operand, operand)} & 7\n")
                elif opcode == 6:  # bdv
                    f.write(f"b = a >> {operand_map.get(operand, operand)}\n")
                elif opcode == 7:  # cdv
                    f.write(f"c = a >> {operand_map.get(operand, operand)}\n")
                idx += 2

    return registers, program


def solve_pt1(registers, program):
    idx = 0
    outputs = []

    while 0 <= idx < len(program) - 1:
        opcode, operand = program[idx:idx+2]
        if opcode == 0: # adv
            registers[4] = registers[4] >> registers.get(operand, operand)
        elif opcode == 1: # bxl
            registers[5] = registers[5] ^ operand
        elif opcode == 2: # bst
            registers[5] = registers.get(operand, operand) & (8-1) # 3 bitmask
        elif opcode == 3: # jnz
            if registers[4] != 0:
                idx = operand
                continue
        elif opcode == 4: # bxc
            registers[5] = registers[5] ^ registers[6]
        elif opcode == 5: # out
            outputs.append(registers.get(operand, operand) & (8-1))
        elif opcode == 6: # bdv
            registers[5] = registers[4] >> registers.get(operand, operand)
        elif opcode == 7:  # cdv
            registers[6] = registers[4] >> registers.get(operand, operand)

        idx += 2

    return ",".join([str(e) for e in outputs])


def solve_pt2(program):
    valid_solutions = [0]
    for r in program[::-1]:
        new_valid_solutions = []
        for solution in valid_solutions:
            for new3bits in range(8):
                new_solution = (solution << 3) | new3bits
                c = new_solution >> ((new_solution & 7) ^ 7)
                b = (new_solution & 7)
                out = (b ^ c) & 7
                if out == r:
                    new_valid_solutions.append(new_solution)
        valid_solutions = new_valid_solutions

    score = min(valid_solutions)
    return score


# PARSE INPUT
registers, program = parse_input()

# PART 1
score = solve_pt1(registers, program)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(program)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass