

from collections import defaultdict


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()

    file_id = 0
    partition_position = 0
    partitions = []
    for p_idx, partition_size_txt in enumerate(input_txt):
        # get file id and increase files count
        partition_size = int(partition_size_txt)
        partition = (partition_position, partition_size, file_id if p_idx % 2 == 0 else None)
        partitions.append(partition)

        # update running values
        partition_position += partition_size
        file_id += 1 if p_idx % 2 == 0 else 0

    return partitions


def solve_pt1(partitions):

    empty_blocks = [p for p in partitions if p[2] is None]
    nonempty_blocks = [p for p in partitions if p[2] is not None]

    # until there are empty blocks before a non-empty one
    candidate_partitions = []
    max_neb_position = max(neb[0] for neb in nonempty_blocks)
    while [eb for eb in empty_blocks if eb[0] < max_neb_position]:
        # get the leftmost empty block
        e_partition_position, e_partition_size, _ = empty_blocks[0]
        empty_blocks = empty_blocks[1:]
        remaining_e_partition_size = e_partition_size

        # get the furthest non-empty file partitions that might fill the empy partition
        num_ne_blocks = len(nonempty_blocks)
        for ne_rev_idx, (ne_partition_position, ne_partition_size, ne_file_id) in enumerate(nonempty_blocks[::-1], 1):
            # if the empty block has been filled, skip
            if remaining_e_partition_size == 0:
                break

            if ne_partition_size <= remaining_e_partition_size:
                # if the furthest block is completely contained, remove it from the end and move it in the empty block
                del nonempty_blocks[num_ne_blocks-ne_rev_idx]
                candidate_partitions.append((e_partition_position + (e_partition_size - remaining_e_partition_size),
                                             ne_partition_size, ne_file_id))

                # reduce emtpy partition size to fill
                remaining_e_partition_size -= ne_partition_size

            else:
                # otherwise move part of its content into the candidate partitions
                candidate_partitions.append((e_partition_position + (e_partition_size - remaining_e_partition_size),
                                             remaining_e_partition_size, ne_file_id))

                # and decrease its size in the original location
                nonempty_blocks[num_ne_blocks-ne_rev_idx] = (ne_partition_position, ne_partition_size - remaining_e_partition_size, ne_file_id)
                remaining_e_partition_size = 0

        max_neb_position = nonempty_blocks[-1][0]

    # update nonempty blocks, adding the candidate partitions and sorting
    nonempty_blocks = nonempty_blocks + candidate_partitions
    nonempty_blocks = sorted(nonempty_blocks, key=lambda x: x[0])

    # TODO: automatically fix last nonempty blocks which leave an empty space
    # currently the result has been obtained manually fixing the list
    for idx in range(len(nonempty_blocks)-1):
        if nonempty_blocks[idx][0] + nonempty_blocks[idx][1] != nonempty_blocks[idx+1][0]:
            print("Warning: non contiguous nonempty blocks.")

    # calculate score
    score = 0
    for ne_position, ne_size, ne_file_id in nonempty_blocks:
        for idx in range(ne_position, ne_position + ne_size):
            score += idx * ne_file_id

    return score


def group_empty_blocks(empty_blocks):
    empty_blocks = sorted(empty_blocks, key=lambda x: x[0])

    # pop the first block
    new_empty_blocks = [empty_blocks[0]]
    del empty_blocks[0]

    while empty_blocks:
        # check if the new block follows the prev one
        if new_empty_blocks[-1][0] + new_empty_blocks[-1][1] == empty_blocks[0][0]:
            new_empty_blocks[-1] = (new_empty_blocks[-1][0], new_empty_blocks[-1][1] + empty_blocks[0][1], None)
        else:
            new_empty_blocks.append(empty_blocks[0])
        del empty_blocks[0]

    return new_empty_blocks


def solve_pt2(partitions):

    empty_blocks = [p for p in partitions if p[2] is None]
    nonempty_blocks = [p for p in partitions if p[2] is not None]

    # count sizes
    empty_sizes_count = defaultdict(int)
    for (e_position, e_size, _) in empty_blocks:
        empty_sizes_count[e_size] += 1

    # try to move each block
    file_blocks = []
    for ne_position, ne_size, ne_file_id in sorted(nonempty_blocks, key=lambda x: x[2], reverse=True):
        for eb_idx, (e_position, e_size, _) in enumerate(empty_blocks):
            if ne_size > e_size or ne_position < e_position:
                continue
            else:
                # move the file block inside the empty block
                file_blocks.append((e_position, ne_size, ne_file_id))

                # add an empty block instead of the file block
                empty_blocks.append((ne_position, ne_size, None))

                # if the empty block has been filled, just delete it. otherwise, modify it
                if ne_size == e_size:
                    del empty_blocks[eb_idx]
                else:
                    empty_blocks[eb_idx] = (e_position + ne_size, e_size - ne_size, None)

                # group empty blocks
                # TODO: optimize empty blocks grouping, or reduce cases where it is really needed
                empty_blocks = group_empty_blocks(empty_blocks)

                # stop iterating over empty blocks
                break
        else:
            # if no empty block has been found that can contain this file, just keep it where it is
            file_blocks.append((ne_position, ne_size, ne_file_id))

    # calculate score
    file_blocks = sorted(file_blocks, key=lambda x: x[0])
    score = 0
    for ne_position, ne_size, ne_file_id in file_blocks:
        for idx in range(ne_position, ne_position + ne_size):
            score += idx * ne_file_id

    return score


# PARSE INPUT
partitions = parse_input()

# PART 1
score = solve_pt1(partitions)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(partitions)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass