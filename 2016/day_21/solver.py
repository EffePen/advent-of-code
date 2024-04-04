import re


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    instructions = input_txt.splitlines()
    return instructions


def apply_instruction(password, instr, reverse=False):
    if instr.startswith("swap"):
        if instr.startswith("swap position"):
            (pos_1, pos_2), = re.findall(r"swap position (\d+) with position (\d+)", instr)
            pos_1, pos_2 = int(pos_1), int(pos_2)
        elif instr.startswith("swap letter"):
            (lett_1, lett_2), = re.findall(r"swap letter (.+) with letter (.+)", instr)
            pos_1 = password.index(lett_1)
            pos_2 = password.index(lett_2)
        else:
            raise ValueError
        password[pos_1], password[pos_2] = password[pos_2], password[pos_1]

    elif instr.startswith("rotate"):
        if instr.startswith("rotate based on position of letter "):
            lett = instr.replace("rotate based on position of letter ", "")
            lett_idx = password.index(lett)
            n_steps = 1 + lett_idx
            if not reverse:
                n_steps += (1 if lett_idx >= 4 else 0)
            else:
                direct_map = {idx: (idx + (1 + idx + (1 if idx >= 4 else 0))) % len(password)
                              for idx in range(len(password))}
                # check that map can be inverted
                srcs = [k for k in direct_map.keys()]
                dsts = [v for v in direct_map.values()]
                assert len(srcs) == len(set(srcs)) == len(dsts) == len(set(dsts))
                inverse_map = {v: k for k, v in direct_map.items()}
                rev_lett_idx = inverse_map[lett_idx]
                if lett_idx >= rev_lett_idx:
                    n_steps = lett_idx - rev_lett_idx
                else:
                    n_steps = len(password) + lett_idx - rev_lett_idx

            direction = "right"
        else:
            (direction, n_steps), = re.findall(r"rotate (.+) (\d+) step.*", instr)
            n_steps = int(n_steps)

        # take into account cycles
        n_steps = n_steps % len(password)
        if reverse:
            direction = "left" if direction == "right" else "right"

        # rotate
        if n_steps == 0:
            pass
        elif direction == "right":
            password = password[-n_steps:] + password[:len(password)-n_steps]
        else:
            password = password[n_steps:] + password[:n_steps]

    elif instr.startswith("reverse positions"):
        (pos_1, pos_2), = re.findall(r"reverse positions (\d+) through (\d+)", instr)
        pos_1, pos_2 = int(pos_1), int(pos_2)
        password = password[:pos_1] + password[pos_1:pos_2+1][::-1] + password[pos_2+1:]

    elif instr.startswith("move position"):
        (pos_1, pos_2), = re.findall(r"move position (\d+) to position (\d+)", instr)
        pos_1, pos_2 = int(pos_1), int(pos_2)
        if reverse:
            pos_1, pos_2 = pos_2, pos_1
        lett = password[pos_1]
        password.remove(lett)
        password.insert(pos_2, lett)
    else:
        raise ValueError

    return password


instructions = parse_input()

# PART 1
password = list("abcdefgh")
for instr in instructions:
    password = apply_instruction(password, instr, reverse=False)
print(f"Part 1 solution: {''.join(password)}")

# PART 2
password = list("fbgdceah")

for instr in instructions[::-1]:
    password = apply_instruction(password, instr, reverse=True)
print(f"Part 2 solution: {''.join(password)}")


if __name__ == "__main__":
    pass