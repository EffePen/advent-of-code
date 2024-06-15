

def get_step_coords_in_spiral(step):
    # The spiral completes squares of side (2n+1), with a reminder that starts
    # at the bottom-right corner (where the y coord is shifted +1),
    # and starts the perimeter of the (2n+3)-side square
    internal_side = int(step ** 0.5)
    # make the side an odd integer
    if internal_side % 2 == 0:
        internal_side -= 1
    remainder = step - internal_side ** 2

    # get bottom-right corner
    external_side = internal_side + 2
    internal_half_side = (internal_side - 1) / 2
    external_half_side = (external_side - 1) / 2

    if remainder == 0:
        x, y = (+ internal_half_side, - internal_half_side)
        return x, y
    else:
        x, y = (+ external_half_side, - external_half_side)

        # move along the perimeter, counter-clock-wise
        for d_idx, (dx, dy) in enumerate([(0, 1), (-1, 0), (0, -1), (1, 0)]):
            delta = min(remainder, external_side - 1)
            x = x + dx * delta
            y = y + dy * delta
            remainder -= delta

            if remainder == 0:
                return x, y


def first_value_above_max_value(max_value):
    new_value = 1
    new_coords = (0, 0)
    prev_values = [(new_coords, new_value)]
    while max_value > new_value:
        step = len(prev_values) + 1
        new_coords = get_step_coords_in_spiral(step=step)
        new_x, new_y = new_coords
        # sum all previous values that are in the new coords surrounding square
        new_value = sum([v for (x, y), v in prev_values
                         if (new_x - 1 <= x <= new_x + 1) and (new_y - 1 <= y <= new_y + 1)])
        prev_values.append((new_coords, new_value))

    return prev_values[-1][1]


# ######## PART 1
input_int = 361527
x, y = get_step_coords_in_spiral(step=input_int)
print("Part 1 solution: ", abs(x) + abs(y))


# ######## PART 2
print("Part 1 solution: ", first_value_above_max_value(max_value=input_int))


if __name__ == "__main__":
    pass