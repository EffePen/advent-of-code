

def parse_input():
    with open("input.txt") as f:
         blocks_str_list = f.read().split()
    blocks_list = [int(e) for e in blocks_str_list]
    return blocks_list


def run_reallocations_p12(banks_list):
    seen_states = []
    n_reallocations = 0
    while True:
        state = "|".join([str(b) for b in banks_list])
        if state in seen_states:
            first_seen_idx = seen_states.index(state)
            return n_reallocations, n_reallocations - first_seen_idx
        seen_states.append(state)

        max_blocks = max(banks_list)
        max_blocks_banks_idx = min([b_idx for b_idx, b in enumerate(banks_list) if b == max_blocks])
        banks_list[max_blocks_banks_idx] = 0
        n_blocks_each = max_blocks // len(banks_list)
        remainder = max_blocks % len(banks_list)
        banks_list = [b + n_blocks_each for b in banks_list]
        for i in range(remainder):
            idx = (max_blocks_banks_idx + 1 + i) % len(banks_list)
            banks_list[idx] += 1
        n_reallocations += 1


# ######## PART 1 & 2
banks_list = parse_input()
n_reallocations, cycle_len = run_reallocations_p12(banks_list=banks_list)
print("Part 1 solution: ", n_reallocations)
print("Part 2 solution: ", cycle_len)


if __name__ == "__main__":
    pass