

import re
from collections import defaultdict


def parse_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    lines = sorted(lines)

    guard_id = None
    guards = defaultdict(lambda: list())
    for l in lines:
        timestamp_str, instr = l.strip("[").split("] ")
        day, hhmm = timestamp_str.split()
        mm = int(hhmm.split(":")[1])
        if instr.startswith("Guard"):
            guard_id, = re.findall("Guard #([0-9]+) begins shift", instr)
            guard_id = int(guard_id)
        elif instr == "falls asleep":
            guards[guard_id].append([mm])
        elif instr == "wakes up":
            guards[guard_id][-1].append(mm)
        else:
            raise ValueError

    return guards


def solve_pt1(guards):
    # get guard sleeping the most
    guards_sleep_time = defaultdict(lambda: 0)
    for gid, sleep_intervals in guards.items():
        for fa, wa in sleep_intervals:
            guards_sleep_time[gid] += wa - fa

    top_gid, top_gid_sleep_time = sorted(guards_sleep_time.items(), key=lambda x: x[1], reverse=True)[0]
    sleep_minutes = defaultdict(lambda: 0)
    for fa, wa in guards[top_gid]:
        for mm in range(fa, wa):
            sleep_minutes[mm] += 1
    top_minute, top_minute_cnt = sorted(sleep_minutes.items(), key=lambda x: x[1], reverse=True)[0]

    score = top_minute * top_gid
    return score


def solve_pt2(guards):
    guards_top_minute = {}
    for gid in guards:
        sleep_minutes = defaultdict(lambda: 0)
        for fa, wa in guards[gid]:
            for mm in range(fa, wa):
                sleep_minutes[mm] += 1
        top_minute, top_minute_cnt = sorted(sleep_minutes.items(), key=lambda x: x[1], reverse=True)[0]
        guards_top_minute[gid] = (top_minute, top_minute_cnt)

    top_gid, (top_minute, v_cnt) = sorted(guards_top_minute.items(), key=lambda x: x[1][1], reverse=True)[0]

    score = top_minute * top_gid
    return score



guards = parse_input()


# ######## PART 1
score = solve_pt1(guards)
print("Part 1 solution: ", score)


## ######## PART 2
score = solve_pt2(guards)
print("Part 2 solution: ", score)


if __name__ == "__main__":
    pass