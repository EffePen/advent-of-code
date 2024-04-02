import re


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    instructions = input_txt.splitlines()
    discs = dict()
    for instr in instructions:
        parsed, = re.findall(r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).", instr)
        disc_id, num_pos, pos_0 = list(map(int, parsed))
        discs[disc_id] = (disc_id, num_pos, pos_0)
    return discs


discs = parse_input()

# PART 1
idx = 0
while True:
    checks = [(pos_0 + disc_id + idx) % num_pos == 0 for (disc_id, num_pos, pos_0) in discs.values()]
    if all(checks):
        break
    else:
        idx += 1

partial_ciclicity_start = idx

print(f"Part 1 solution: {partial_ciclicity_start}")

# PART 2
final_disc_id = len(discs) + 1
final_disc_num_pos = 11
final_disc_pos_0 = 0

partial_ciclicity = 1
for (disc_id, num_pos, pos_0) in discs.values():
    partial_ciclicity *= num_pos

partial_cycle_idx = 0
while True:
    idx = partial_ciclicity_start + partial_cycle_idx * partial_ciclicity
    if (final_disc_pos_0 + final_disc_id + idx) % final_disc_num_pos == 0:
        break
    else:
        partial_cycle_idx += 1

full_ciclicity_start = idx
print(f"Part 2 solution: {full_ciclicity_start}")


if __name__ == "__main__":
    pass