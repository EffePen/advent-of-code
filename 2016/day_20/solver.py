

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    ranges = sorted([[int(e) for e in l.split("-")] for l in input_txt.splitlines()], key=lambda x: x[0])
    return ranges


ranges = parse_input()

# PART 1
min_allowed_ip = 0
ranges_to_check = ranges
while ranges_to_check:
    ranges_including_min = [r for r in ranges_to_check if r[0] <= min_allowed_ip <= r[1]]
    if ranges_including_min:
        min_allowed_ip = max([r_max for r_min, r_max in ranges_including_min]) + 1
        ranges_to_check = [r for r in ranges_to_check if r[1] >= min_allowed_ip]
    else:
        break

print(f"Part 1 solution: {min_allowed_ip}")

# PART 2
min_ip = 0
max_ip = 4294967295
allowed_ips = 0
last_min_allowed_ip = 0
last_max_allowed_ip = 0
ranges_to_check = ranges
while ranges_to_check:
    ranges_including_min = [r for r in ranges_to_check if r[0] <= last_min_allowed_ip <= r[1]]
    if ranges_including_min:
        # if min is included in blacklist ranges, change it to max + 1
        last_min_allowed_ip = +1 + max([r_max for r_min, r_max in ranges_including_min])
    else:
        # if min is not included in blacklist ranges, calc upper bound, increase allowed counter and update min
        # as next blacklist range upper bound + 1
        next_blacklist_range = [r for r in ranges_to_check if r[0] >= last_min_allowed_ip][0]
        last_max_allowed_ip = -1 + next_blacklist_range[0]
        allowed_ips += (last_max_allowed_ip - last_min_allowed_ip + 1)
        last_min_allowed_ip = next_blacklist_range[1] + 1
    ranges_to_check = [r for r in ranges_to_check if r[1] >= last_min_allowed_ip]

max_blacklisted_ip = max([r_max for r_min, r_max in ranges])
allowed_ips += (max_ip - (max_blacklisted_ip + 1) + 1)

print(f"Part 2 solution: {allowed_ips}")


if __name__ == "__main__":
    pass