

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    reindeers = []
    for line_txt in input_txt.splitlines():
        line_txt = line_txt.replace("can fly ", "").replace("km/s for ", "").replace("seconds, but then must rest for ", "").replace(" seconds.", "")
        rid, flight_speed_txt, flight_time_txt, rest_time_txt = line_txt.split()
        flight_speed, flight_time, rest_time = map(int, [flight_speed_txt, flight_time_txt, rest_time_txt])
        reindeers.append((rid, flight_speed, flight_time, rest_time))
    return reindeers


def part1(total_time, reindeers):
    max_dist = 0
    for (rid, flight_speed, flight_time, rest_time) in reindeers:
        cycle_time = flight_time + rest_time
        num_cycles = total_time // cycle_time
        last_cycle_time = total_time % cycle_time
        dist = num_cycles * flight_speed * flight_time + flight_speed * min(flight_time, last_cycle_time)
        max_dist = max(dist, max_dist)
    return max_dist

def part2(total_time, reindeers):
    dists = {r[0]: 0 for r in reindeers}
    scores = {r[0]: 0 for r in reindeers}
    for curr_time in range(total_time):
        # update distance for each reindeer
        for (rid, flight_speed, flight_time, rest_time) in reindeers:
            cycle_time = flight_time + rest_time
            curr_cycle_time = curr_time % cycle_time
            if curr_cycle_time < flight_time:
                dists[rid] += flight_speed

        # increase score of reindeer at max dist
        max_dist = max(dists.values())
        for rid in dists:
            if dists[rid] == max_dist:
                scores[rid] += 1
    return scores

# input
total_time = 2503
reindeers = parse_input()

# part 1
max_dist = part1(total_time, reindeers)
print("Part 1:", max_dist)

# part 2
scores = part2(total_time, reindeers)
print("Part 2:", max(scores.values()))

if __name__ == "__main__":
    pass
