

def parse_input():
    with open("input.txt") as f:
        moves = f.read().split(",")
    return moves


def execute_dance(p_list, moves):
    for move in moves:
        if move.startswith("s"):
            size = int(move[1:])
            p_list = p_list[-size:] + p_list[:-size]
        else:
            if move.startswith("p"):
                p1, p2 = move[1:].split("/")
                p1_idx = p_list.index(p1)
                p2_idx = p_list.index(p2)
            elif move.startswith("x"):
                p1_idx_str, p2_idx_str = move[1:].split("/")
                p1_idx = int(p1_idx_str)
                p2_idx = int(p2_idx_str)
            else:
                raise ValueError
            p_list[p1_idx], p_list[p2_idx] = p_list[p2_idx], p_list[p1_idx]
    return p_list


def execute_bln_dances(p_list, moves):
    prev_configs = ["".join(p_list)]
    for idx in range(1_000_000_000):
        p_list = execute_dance(p_list, moves)
        p_list_str = "".join(p_list)
        if p_list_str in prev_configs:
            offset = prev_configs.index(p_list_str)
            cyclicity = 1 + idx - offset
            final_idx = (1_000_000_000 - offset) % cyclicity
            return prev_configs[offset + final_idx]
        else:
            prev_configs.append(p_list_str)

    return p_list


moves = parse_input()


# ######## PART 1
p_list = list("abcdefghijklmnop")
p_list = execute_dance(p_list, moves)
print("Part 1 solution: ", "".join(p_list))

# ######## PART 2
p_list = list("abcdefghijklmnop")
p_list = execute_bln_dances(p_list, moves)
print("Part 2 solution: ", "".join(p_list))


if __name__ == "__main__":
    pass