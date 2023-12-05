
import sys


def get_intersection(interval1, interval2):
    new_min = max(interval1[0], interval2[0])
    new_max = min(interval1[1], interval2[1])
    return (new_min, new_max) if new_min <= new_max else None


def get_next_ranges(item, source_input_interval, values_mapping):
    output_intervals = []
    destination_item, intervals = values_mapping[item]
    for (source_start, source_end, translation) in intervals:
        intersect_source_interval = get_intersection(source_input_interval[:2],
                                                     (source_start, source_end))
        # if there is an intersection, transform it to destination interval (translate)
        if intersect_source_interval:
            intersect_destination_interval = [e+translation for e in intersect_source_interval]
            output_intervals.append(intersect_destination_interval)

    return destination_item, output_intervals


def get_values_mapping(maps_raw):
    values_mapping = {}
    for m_raw in maps_raw.split("\n\n"):
        # get items mapping
        source_item, destination_item = m_raw.split(" map:")[0].strip().split("-to-")

        # get value mapping
        tmp_intervals = []
        for map_line in m_raw.split(" map:")[1].strip().split("\n"):
            destination_start, source_start, m_range = [int(e) for e in map_line.split()]
            source_end = source_start + m_range
            translation = destination_start - source_start
            tmp_intervals.append((source_start, source_end, translation))

        # sort intervals (assuming no overlaps)
        sorted_tmp_intervals = sorted(tmp_intervals, key=lambda x: x[0])

        intervals = []
        # Add leftmost interval
        min_source_start = min([e[0] for e in sorted_tmp_intervals])
        intervals.append((-sys.maxsize, min_source_start, 0))

        # Add sorted intervals
        for curr_idx in range(len(sorted_tmp_intervals)):
            curr_interval = sorted_tmp_intervals[curr_idx]
            intervals.append(curr_interval)

            # If there is a gap between current and next interval, create interval with 0 translation
            if curr_idx < len(sorted_tmp_intervals) - 1:
                next_interval = sorted_tmp_intervals[curr_idx + 1]
                curr_end = curr_interval[1]
                next_start = next_interval[0]

                if curr_end < next_start:
                    intervals.append((curr_end, next_start, 0))

        # Add rightmost interval
        max_source_end = max([e[1] for e in sorted_tmp_intervals])
        intervals.append((max_source_end, sys.maxsize, 0))

        # Check that sorted intervals are all continuous
        assert all([intervals[idx][1] == intervals[idx + 1][0]
                    for idx in range(len(intervals) - 1)])

        values_mapping[source_item] = (destination_item, intervals)
    return values_mapping