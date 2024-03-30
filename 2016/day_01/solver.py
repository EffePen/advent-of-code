

import math


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    steps = [(e[0], int(e[1:])) for e in input_txt.split(", ")]
    return steps


def rotate_vector(vector, angle):
    x = vector[0] * math.cos(angle) - vector[1] * math.sin(angle)
    y = vector[0] * math.sin(angle) + vector[1] * math.cos(angle)
    return [x, y]

# PARSE INPUT
steps = parse_input()

# PART 1
initial_position = (0, 0)
initial_direction = [1, 0]

dir_angle_map = {"R": math.pi/2, "L": -math.pi/2}
direction = initial_direction
position = initial_position

hq_position = None
positions = [initial_position]
for dir, length in steps:
    angle = dir_angle_map[dir]
    direction = rotate_vector(direction, angle=angle)

    new_positions = [(round(position[0] + direction[0]*delta), round(position[1] + direction[1]*delta)) for delta in range(1, length+1)]
    if hq_position is None and set(new_positions) & set(positions):
        hq_position, = set(new_positions) & set(positions)

    positions.extend(new_positions)
    position = positions[-1]

manhattan_distance = abs(initial_position[0] - position[0]) + abs(initial_position[1] - position[1])
print(f"Part 1 solution: {round(manhattan_distance)}")

manhattan_distance = abs(initial_position[0] - hq_position[0]) + abs(initial_position[1] - hq_position[1])
print(f"Part 2 solution: {round(manhattan_distance)}")


if __name__ == "__main__":
    pass