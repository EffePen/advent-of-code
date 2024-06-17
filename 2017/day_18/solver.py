

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


def execute_p1(instructions, registers):
    last_sound = None
    idx = 0
    while 0 <= idx < len(instructions):
        instr = instructions[idx]
        idx += 1
        instr_prefix, values = instr.split(maxsplit=1)
        if instr_prefix in ("snd", "rcv"):
            val_str = values
            val = get_value(val_str, registers)
            if instr_prefix == "snd":
                last_sound = val
            elif val != 0:
                return last_sound
        else:
            val1_str, val2_str = values.split()
            val1 = get_value(val1_str, registers)
            val2 = get_value(val2_str, registers)
            if instr_prefix == "set":
                registers[val1_str] = val2
            elif instr_prefix == "add":
                registers[val1_str] += val2
            elif instr_prefix == "mul":
                registers[val1_str] *= val2
            elif instr_prefix == "mod":
                registers[val1_str] %= val2
            elif instr_prefix == "jgz":
                if val1 > 0:
                    idx += val2 - 1
            else:
                raise ValueError(f"Unknown instruction: {instr_prefix}")


def generator_p2(instructions, registers_a, buffer_a, buffer_b):
    idx = 0
    snd_counter = 0
    while 0 <= idx < len(instructions):
        instr = instructions[idx]
        idx += 1
        instr_prefix, values = instr.split(maxsplit=1)
        if instr_prefix in ("snd", "rcv"):
            val_str = values
            val = get_value(val_str, registers_a)
            if instr_prefix == "snd":
                buffer_b.append(val)
                snd_counter += 1
            else:
                if len(buffer_a) == 0:
                    yield snd_counter
                    # if the buffer is still empty at resume,
                    # return a negative value
                    while len(buffer_a) == 0:
                        yield -1
                registers_a[val_str] = buffer_a.pop(0)
        else:
            val1_str, val2_str = values.split()
            val1 = get_value(val1_str, registers_a)
            val2 = get_value(val2_str, registers_a)
            if instr_prefix == "set":
                registers_a[val1_str] = val2
            elif instr_prefix == "add":
                registers_a[val1_str] += val2
            elif instr_prefix == "mul":
                registers_a[val1_str] *= val2
            elif instr_prefix == "mod":
                registers_a[val1_str] %= val2
            elif instr_prefix == "jgz":
                if val1 > 0:
                    idx += val2 - 1
            else:
                raise ValueError(f"Unknown instruction: {instr_prefix}")


def execute_p2(instructions):
    registers_0 = collections.defaultdict(lambda: 0)
    registers_1 = collections.defaultdict(lambda: 0)
    registers_0["p"] = 0
    registers_1["p"] = 1
    buffer_0 = list()
    buffer_1 = list()
    generator_0 = generator_p2(instructions, registers_0, buffer_0, buffer_1)
    generator_1 = generator_p2(instructions, registers_1, buffer_1, buffer_0)

    gen_1_counter = 0
    while True:
        cnt_0 = next(generator_0)
        cnt_1 = next(generator_1)
        if cnt_1 != -1:
            gen_1_counter = cnt_1

        if (cnt_0 == -1) and (cnt_1 == -1):
            break
    return gen_1_counter


instructions = parse_input()


# ######## PART 1
registers = collections.defaultdict(lambda: 0)
sound = execute_p1(instructions, registers)
print("Part 1 solution: ", sound)

# ######## PART 2
gen_1_counter = execute_p2(instructions)
print("Part 2 solution: ", gen_1_counter)


if __name__ == "__main__":
    pass