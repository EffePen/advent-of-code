

import string
from collections import Counter


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    rooms_txt = input_txt.splitlines()
    rooms = []
    for r_txt in rooms_txt:
        code_raw, hash_raw = r_txt.split("[")
        hash = hash_raw.strip("]")
        letters_code, room_code_txt = code_raw.rsplit("-", 1)
        room_code = int(room_code_txt)
        rooms.append((letters_code, room_code, hash))
    return rooms


# PARSE INPUT
rooms = parse_input()
alphabet = string.ascii_lowercase
alphabet_len = len(alphabet)

ok_rooms = []
score = 0
for letters_code, room_code, hash in rooms:
    letters = letters_code.replace("-", "")
    counter = sorted(Counter(letters).most_common(), key=lambda x: (-x[1], x[0]))
    actual_hash = "".join([e[0] for e in counter[:5]])
    if actual_hash == hash:
        score += room_code

        # map code
        new_alphabet_map = {l: alphabet[(l_idx + room_code) % alphabet_len]
                            for l_idx, l in enumerate(alphabet)}
        new_letters_code = "".join([new_alphabet_map.get(l, " ") for l in letters_code])
        if "north" in new_letters_code:
            print(new_letters_code, room_code)
            part2_score = room_code

# PART 1
print(f"Part 1 solution: {score}")

# PART 2
print(f"Part 2 solution: {part2_score}")

if __name__ == "__main__":
    pass