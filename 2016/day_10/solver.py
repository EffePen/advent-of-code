import re


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    instructions = input_txt.splitlines()
    return instructions


objs = {
    "bot": {},
    "output": {},
}

# PART 1
instructions = parse_input()

part1_done = False
part2_done = False
while not (part1_done and part2_done):
    for instr in instructions:
        if instr.startswith("value"):
            (val_id, bot_id), = re.findall(r"value (\d+) goes to bot (\d+)", instr)
            if bot_id not in objs["bot"]:
                objs["bot"][bot_id] = set()
            if len(objs["bot"][bot_id]) < 2:
                objs["bot"][bot_id].add(int(val_id))
        else:
            parsed, = re.findall(r"bot (\d+) gives low to (.+) (\d+) and high to (.+) (\d+)", instr)
            (src_bot_id, low_dst_kind, low_dst_id, high_dst_kind, high_dst_id) = parsed
            src_bot_values = objs["bot"].get(src_bot_id, set())

            if len(src_bot_values) == 2:
                if {61, 17} <= src_bot_values:
                    part1_done = True
                    part1_solution = src_bot_id

                if all([idx in objs["output"] for idx in ['0', '1', '2']]):
                    part2_done = True
                    e0, = objs["output"]['0']
                    e1, = objs["output"]['1']
                    e2, = objs["output"]['2']
                    part2_solution =  e0 * e1 * e2

                #objs["bot"][src_bot_id] = []
                if low_dst_id not in objs[low_dst_kind]:
                    objs[low_dst_kind][low_dst_id] = set()
                if high_dst_id not in objs[high_dst_kind]:
                    objs[high_dst_kind][high_dst_id] = set()
                objs["bot"][src_bot_id] = set()
                objs[low_dst_kind][low_dst_id].add(min(src_bot_values))
                objs[high_dst_kind][high_dst_id].add(max(src_bot_values))

print(f"Part 1 solution: {part1_solution}")
print(f"Part 1 solution: {part2_solution}")

if __name__ == "__main__":
    pass