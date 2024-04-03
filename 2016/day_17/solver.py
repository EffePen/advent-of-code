import hashlib

input_salt = "yjjvjgan"


def get_open_doors(path):
    h = hashlib.md5(f"{input_salt}{path}".encode()).hexdigest()
    dirs_open = [int(c, 16) >= 11 for c in h[:4]]
    return dict(zip("UDLR", dirs_open))


dir_delta_dict = {
    'U': (0, -1),
    'D': (0, +1),
    'L': (-1, 0),
    'R': (+1, 0),
}

# PART 1 & 2
initial_pos = (0, 0)
final_pos = (3, 3)
possible_paths = ['']
possible_positions = [initial_pos]
pos_path_list = list(zip(possible_positions, possible_paths))
longest_path_len = 0

reached_exit = False
while not reached_exit or pos_path_list:
    new_pos_path_list = []
    for possible_pos, possible_path in pos_path_list:
        doors_dict = get_open_doors(possible_path)
        x, y = possible_pos

        for door_dir, door_is_open in doors_dict.items():
            dx, dy = dir_delta_dict[door_dir]
            new_pos = (x + dx, y + dy)
            new_path = possible_path + door_dir
            if not door_is_open or not (0 <= new_pos[0] < 4 and 0 <= new_pos[1] < 4):
                continue
            elif new_pos == final_pos:
                if not reached_exit:
                    reached_exit = True
                    shortest_path = new_path
                longest_path_len = max(longest_path_len, len(new_path))
            else:
                new_pos_path_list.append((new_pos, new_path))

    pos_path_list = new_pos_path_list


print(f"Part 1 solution: {shortest_path}")
print(f"Part 2 solution: {longest_path_len}")


if __name__ == "__main__":
    pass