

def execute_pt1(steps_forward, n_iterations, num_to_find):
    circular_buffer = [0]
    next_idx = 0
    for value in range(1, n_iterations+1):
        next_idx = 1 + (next_idx + steps_forward) % value
        circular_buffer.insert(next_idx, value)
    last_idx = circular_buffer.index(num_to_find)
    return circular_buffer[(last_idx+1) % len(circular_buffer)]


def execute_pt2(steps_forward, n_iterations):
    next_idx = 0
    zero_idx = 0
    next_to_zero_value = None
    for value in range(1, n_iterations+1):
        next_idx = 1 + (next_idx + steps_forward) % value
        # Only check if the next idx would be current zero idx of precede it
        # In the first case, update che next to zero value
        # In the second case, shift the zero idx
        if (next_idx - 1) <= zero_idx:
            if (next_idx - 1) == zero_idx:
                next_to_zero_value = value
            else:
                zero_idx += 1
    return next_to_zero_value


def execute_pt2_optimized(steps_forward, n_iterations):
    next_idx = 0
    zero_idx = 0
    next_to_zero_value = None
    for value in range(1, n_iterations+1):
        next_idx = 1 + (next_idx + steps_forward) % value
        # It can never happen that next_idx == 0
        # => you just need to check if next_idx == 1, and in case update che next to zero value
        if next_idx == 1:
            next_to_zero_value = value
    return next_to_zero_value


steps_forward = 356

# ######## PART 1
n_iterations = 2017
num_to_find = 2017
count = execute_pt1(steps_forward, n_iterations, num_to_find)
print("Part 1 solution: ", count)


# ######## PART 1
n_iterations = 50_000_000
count = execute_pt2_optimized(steps_forward, n_iterations)
print("Part 2 solution: ", count)

if __name__ == "__main__":
    pass
