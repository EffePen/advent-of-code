

with open("a_input.txt") as f:
    input_txt = f.read()

status_map = {"#": 1, ".": -1, "?": 0}
rev_map = {v: k for k, v in status_map.items()}


def get_next_lists(tmp_lists, idx, num_free_spaces_tot, num_space_segments):
    lists = []
    for ls in tmp_lists:
        # min 1 space if in between
        min_spaces = [0 if tmp_idx == 0 or tmp_idx == num_space_segments - 1 else 1 for tmp_idx in range(idx + 1)]
        num_spaces_left = num_free_spaces_tot - (sum(ls) - sum(min_spaces[:-1]))
        for new_num_spaces in range(min_spaces[-1], min_spaces[-1] + num_spaces_left + 1):
            lists.append(ls + [new_num_spaces])

    if all(len(ls) == num_space_segments for ls in lists):
        return lists
    elif any(len(ls) == num_space_segments for ls in lists):
        raise RuntimeError
    else:
        return get_next_lists(lists, idx + 1, num_free_spaces_tot, num_space_segments)


count_list = []
springs_rows = input_txt.splitlines()
for springs_row in springs_rows:
    spring_map, broken_sizes_str = springs_row.split()
    broken_segment_sizes = [int(e) for e in broken_sizes_str.split(",")]
    spring_sequence = [status_map[e] for e in spring_map]

    num_broken_segments = len(broken_segment_sizes)
    num_space_segments_in_between = num_broken_segments - 1 # at least size 1
    num_space_segments = num_space_segments_in_between + 2 # + the left and right space segments
    spring_len = len(spring_sequence)

    num_free_spaces_tot = spring_len - sum(broken_segment_sizes) - num_space_segments_in_between

    possible_spaces_list = get_next_lists([[]], idx=0,
                                          num_free_spaces_tot=num_free_spaces_tot,
                                          num_space_segments=num_space_segments)
    # for eac possible sequence, check if all elements of the sequence are compatible
    # (the product must be 1 (same type) or 0 (one is ?))
    tmp_count = 0
    possible_sequences_str = []
    for space_segment_sizes in possible_spaces_list:
        possible_sequence = []
        for space_segment_size, broken_segment_size in zip(space_segment_sizes[:-1], broken_segment_sizes):
            possible_sequence += [-1] * space_segment_size + [1] * broken_segment_size
        possible_sequence += [-1] * space_segment_sizes[-1]
        possible_sequence_str = "".join(rev_map[e] for e in possible_sequence)
        possible_sequences_str.append(possible_sequence_str)

        if all([pe * se >= 0 for pe, se in zip(possible_sequence, spring_sequence)]) \
                and len(possible_sequence) == spring_len:
            tmp_count += 1

    count_list.append(tmp_count)

print(sum(count_list))

if __name__ == "__main__":
    pass
