

def parse_input():
    with open("input.txt") as f:
        jumps_str_list = f.readlines()
    jumps_list = [int(e) for e in jumps_str_list]
    return jumps_list


def run_jumps_p1(jumps_list):
    idx = 0
    n_steps = 0
    while 0 <= idx < len(jumps_list):
        jump = jumps_list[idx]
        jumps_list[idx] += 1
        idx += jump
        n_steps += 1
    return n_steps


def run_jumps_p2(jumps_list):
    idx = 0
    n_steps = 0
    while 0 <= idx < len(jumps_list):
        jump = jumps_list[idx]
        if jump >= 3:
            jumps_list[idx] -= 1
        else:
            jumps_list[idx] += 1
        idx += jump
        n_steps += 1
    return n_steps


# ######## PART 1
jumps_list = parse_input()
n_steps = run_jumps_p1(jumps_list=jumps_list)
print("Part 1 solution: ", n_steps)


# ######## PART 2
jumps_list = parse_input()
n_steps = run_jumps_p2(jumps_list=jumps_list)
print("Part 2 solution: ", n_steps)


if __name__ == "__main__":
    pass