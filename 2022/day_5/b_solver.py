
import re

with open('a_input.txt') as f:
    input_txt = f.read()

cargo_drawing, moves_txt = input_txt.split("\n\n")

# reverse to start from bottom and exclude slot indices
cargo_drawing_lines = cargo_drawing.splitlines()[::-1]
piles_drawing_lines = cargo_drawing_lines[1:]
slot_ids_line = cargo_drawing_lines[0]

slot_piles_dict = {}
slot_string_idx = 1

while slot_string_idx < len(slot_ids_line):
    slot_id = int(slot_ids_line[slot_string_idx])
    slot_piles_dict[slot_id] = []

    for pdl in piles_drawing_lines:
        try:
            slot_element = pdl[slot_string_idx]
            if slot_element != " ":
                slot_piles_dict[slot_id].append(slot_element)
        except IndexError:
            break
    slot_string_idx += 4

for move in moves_txt.splitlines():
    cnt, src_slot_id, dst_slot_id = [int(i) for i in re.findall("[0-9]+", move)]

    tmp_pile = []
    for _ in range(cnt):
        e = slot_piles_dict[src_slot_id].pop()
        tmp_pile.append(e)
    slot_piles_dict[dst_slot_id].extend(tmp_pile[::-1])

msg = []
for slot_id in range(1, len(slot_piles_dict)+1):
    msg.append(slot_piles_dict[slot_id][-1])

print("".join(msg))

if __name__ == "__main__":
    pass
