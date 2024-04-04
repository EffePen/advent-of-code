
num_elves = 3018458





#
remaining_elves = num_elves

idx = 0
odd_counter = 0
first_of_list = 1
while remaining_elves > 1:
    remainder_elves = remaining_elves % 2
    remaining_elves = remaining_elves // 2 + remainder_elves
    # at each iteration, last of the list is either removed (if at an even position) or moved to first position
    if remainder_elves:
        # remaining last of the list becomes first
        first_of_list = num_elves - (2**idx if idx > 0 else 0)
        odd_counter += 1
    idx += 1

    if odd_counter >= remaining_elves:
        a = 1

print(f"Part 1 solution: {first_of_list}")


if __name__ == "__main__":
    pass