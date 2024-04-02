import copy
import json


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    floors_config = json.loads(input_txt)
    floors_config = [{tuple(e) for e in l} for l in floors_config]
    return floors_config


def is_env_safe(env):
    generators = {e[0] for e in env if e[1] == "G"}
    if generators:
        microchips = {e[0] for e in env if e[1] == "M"}
        return len(microchips - generators) == 0
    else:
        return True


def is_final_move(curr_config):
    return len(curr_config[0]) == 0 and len(curr_config[1]) == 0 and len(curr_config[2]) == 0


def get_allowed_moves(curr_floor, curr_config, visited_configs):
    possible_next_floors = {e for e in [curr_floor - 1, curr_floor + 1] if 0 <= e <= 3}
    curr_floor_objects = curr_config[curr_floor]

    possible_next_moves = []
    # pair all possible objects (same object pairs are collapsed)
    for obj1 in curr_floor_objects:
        for obj2 in curr_floor_objects:
            possible_next_load = tuple(sorted({obj1, obj2}))
            # check if the load would be safe
            if is_env_safe(possible_next_load):
                # check if current floor would be safe
                possible_curr_floor_objects = curr_floor_objects - set(possible_next_load)
                if is_env_safe(possible_curr_floor_objects):
                    # check if each next floors would be safe
                    for next_floor in possible_next_floors:
                        # merge load with next floor and check if would be safe
                        possible_next_floor_objects = curr_config[next_floor] | set(possible_next_load)
                        if is_env_safe(possible_next_floor_objects):
                            next_config = copy.deepcopy(curr_config)
                            next_config[curr_floor] = possible_curr_floor_objects
                            next_config[next_floor] = possible_next_floor_objects
                            if freeze_config(next_config) not in visited_configs:
                                possible_next_moves.append((next_floor, next_config))

    return possible_next_moves


def freeze_config(config):
    return (tuple(sorted(e)) for e in config)


config = parse_input()
visited_configs = [freeze_config(config)]
possible_next_moves = get_allowed_moves(curr_floor=0, curr_config=config, visited_configs=visited_configs)
counter = 1
while True:
    new_possible_next_moves = []
    for curr_floor, curr_config in possible_next_moves:
        visited_configs.append(freeze_config(curr_config))
        new_possible_next_moves += get_allowed_moves(curr_floor, curr_config, visited_configs)
    possible_next_moves = new_possible_next_moves
    counter += 1
    a = 1
    if any([is_final_move(move[1]) for move in possible_next_moves]):
        break

print(f"Part 1 solution: {counter}")
#print(f"Part 1 solution: {part2_solution}")

if __name__ == "__main__":
    pass