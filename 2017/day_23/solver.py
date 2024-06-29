

import collections


def parse_input():
    with open("input.txt") as f:
        instructions = f.read().splitlines()
    # remove inline comments
    instructions = [instr.split("#")[0].strip() for instr in instructions]
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


def execute_p2_expanded():
    b = 57 * 100 + 100_000
    c = b + 17000
    h = 0
    while True:
        f = 1
        d = 2
        while True:
            e = 2
            while True:
                if d * e == b:
                    f = 0
                e += 1
                if e == b: break
            d += 1
            if d == b: break
        if f == 0:
            h += 1
        if b == c:
            break
        b += 17
    return h


def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))


def execute_p2_optimized():
    b = 57 * 100 + 100_000
    c = b + 17000
    if (c - b) % 17 != 0:
        assert False
    outer_loop_steps = (c - b) // 17 + 1
    h = 0
    for b_idx in range(outer_loop_steps):
        b += 17
        # the following code translates to "if b is not prime => f = 0"
        # => "if b is not prime => h += 1"
        # f = 1
        # for d in range(2, b+1):
        #     for e in range(2, b+1):
        #         if d * e == b:
        #             f = 0
        # if f == 0:
        #     h += 1
        if not is_prime(b):
            h += 1

    return h


instructions = parse_input()


# ######## PART 1
registers = collections.defaultdict(lambda: 0)
instr_count = execute_p1(instructions, registers)
print("Part 1 solution: ", instr_count["mul"])


# ######## PART 2
score = execute_p2_optimized()
print("Part 1 solution: ", score)



if __name__ == "__main__":
    pass