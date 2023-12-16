

with open("a_input.txt") as f:
    input_txt = f.read()


count_list = []
springs_rows = input_txt.splitlines()
for springs_row in springs_rows:
    spring_map, broken_sizes_str = springs_row.split()
    # TODO: add x5
    #spring_map = "?".join([spring_map]*5)
    #broken_sizes_str = ",".join([broken_sizes_str]*5)
    broken_segment_sizes = [int(e) for e in broken_sizes_str.split(",")]

    # get candidate interval for each segment, given by the basic constraint of other segments and gaps
    broken_segment_intervals = []
    for idx, bss in enumerate(broken_segment_sizes):
        bs_intervals = []
        # prev/next broken sizes + min 1 gap per segment
        prev_size_constraint = sum(broken_segment_sizes[:idx])   + len(broken_segment_sizes[:idx])
        next_size_constraint = sum(broken_segment_sizes[idx+1:]) + len(broken_segment_sizes[idx+1:])
        broken_segment_intervals.append([(prev_size_constraint, len(spring_map) - next_size_constraint)])

    # apply constraints for each element in the spring
    min_contig_broken = 99999
    for se_idx, spring_element in enumerate(spring_map):
        # if "?" => no constraints
        if spring_element == "?":
            continue

        if spring_element != "#":
            min_contig_broken = 99999

        # otherwise, iterate over each segment candidate intervals to update them according to constraint
        for seg_idx, (segment_size, intervals) in enumerate(zip(broken_segment_sizes, broken_segment_intervals)):
            new_intervals = []
            for interval in intervals:
                # if constraining element not in interval, skip
                if not (interval[0] <= se_idx < interval[1]):
                    new_intervals.append(interval)
                else:
                    # "." (not-broken) split the candidate broken interval in 2
                    if spring_element == ".":
                        new_intervals.extend([(interval[0], se_idx), (se_idx+1, interval[1])])
                    # "#" (broken) constraints the segment to contain it or to be at least 1 step away
                    # take into account if the last elements were broken as well (stronger constraint on upper idx)
                    elif spring_element == "#":
                        # 1 step away segments
                        new_intervals.extend([(interval[0], se_idx-1), (se_idx+2, interval[1])])
                        # containing segment (element can be at most at the beginning or at the end of segment)
                        new_intervals.extend([(max(interval[0], se_idx - segment_size + 1),
                                               min(interval[1], min(se_idx, min_contig_broken) + segment_size))])
                        min_contig_broken = se_idx
                    else:
                        raise RuntimeError

            # Discard the parts that are already too small to contain current segment
            filtered_new_intervals = [i for i in new_intervals if (i[1] - i[0]) >= segment_size]

            # update segments
            broken_segment_intervals[seg_idx] = filtered_new_intervals

    for _ in range(2):
        # each segment can start at most 2 blocks from the min idx + segment size + 1 of the previous one
        last_min_idx = -1
        for seg_idx, (segment_size, intervals) in enumerate(zip(broken_segment_sizes, broken_segment_intervals)):
            new_intervals = [(max(idx_min, last_min_idx), idx_max) for idx_min, idx_max in intervals]

            # re-filter based on size
            filtered_new_intervals = [i for i in new_intervals if (i[1] - i[0]) >= segment_size]
            broken_segment_intervals[seg_idx] = filtered_new_intervals

            last_min_idx = min([idx_min + segment_size + 1 for idx_min, _ in intervals])

        # each segment can start at most 2 blocks from the max idx - segment size of the next one
        next_max_idx = len(spring_map) + 1
        for seg_idx, (segment_size, intervals) in list(enumerate(zip(broken_segment_sizes, broken_segment_intervals)))[::-1]:
            new_intervals = [(idx_min, min(idx_max, next_max_idx)) for idx_min, idx_max in intervals]

            # re-filter based on size
            filtered_new_intervals = [i for i in new_intervals if (i[1] - i[0]) >= segment_size]
            broken_segment_intervals[seg_idx] = filtered_new_intervals

            next_max_idx = max([idx_max - segment_size - 1 for _, idx_max in intervals])

    # calc combinations
    final_segment_size_intervals = list(zip(broken_segment_sizes, broken_segment_intervals))

    overlapping_segment_groups = [[0]]
    for seg_idx in range(1, len(final_segment_size_intervals)):
        overlapping_last = False
        # TODO: get overlapping groups and calculate joint configs

    max_segment_configs = 1
    for seg_idx, (segment_size, intervals) in enumerate(zip(broken_segment_sizes, broken_segment_intervals)):
        curr_seg_configs = 0

        # check overlaps. If no overlaps easy to calc
        for interval in intervals:
            curr_seg_configs = interval[1] - interval[0] - segment_size + 1
        max_segment_configs *= curr_seg_configs

    print(max_segment_configs)

if __name__ == "__main__":
    pass
