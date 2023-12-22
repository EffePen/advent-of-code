import sys


def parse_file():
    with open("a_input.txt") as f:
        input_txt = f.read()

    # read each brick starting status
    bricks = []
    for b_idx, brick_row in enumerate(input_txt.splitlines()):
        start_str, end_str = brick_row.split("~")
        x1, y1, z1 = [int(i) for i in start_str.split(",")]
        x2, y2, z2 = [int(i) for i in end_str.split(",")]
        bricks.append((b_idx, ((x1, y1, z1), (x2, y2, z2))))
    return bricks


def get_brick_alignment_idx(brick):
    (x1, y1, z1), (x2, y2, z2) = brick
    if x1 != x2:
        return 0
    elif y1 != y2:
        return 1
    elif z1 != z2:
        return 2
    else:
        # single block, return z-align
        return 2


def bricks_h_intersect(brick1, brick2):
    align_idx1 = get_brick_alignment_idx(brick1)
    align_idx2 = get_brick_alignment_idx(brick2)

    # if any is z-aligned, check single valid x-y
    if (align_idx1 == 2) or (align_idx2 == 2):
        lim_brick = brick1 if (align_idx1 == 2) else brick2
        other_brick = brick2 if (align_idx1 == 2) else brick1
        (xlim, ylim, _), _ = lim_brick
        (x1, y1, z1), (x2, y2, z2) = other_brick
        h_intersect = (x1 <= xlim <= x2) and (y1 <= ylim <= y2)
    # if none is z-aligned, and alignment is different, find intersection point
    elif align_idx1 != align_idx2:
        limy_brick = brick1 if (align_idx1 == 0) else brick2
        limx_brick = brick2 if (align_idx1 == 0) else brick1
        (x1, ylim, _), (x2, _, _) = limy_brick
        (xlim, y1, _), (_, y2, _) = limx_brick
        h_intersect = (x1 <= xlim <= x2) and (y1 <= ylim <= y2)
    # if both are x-aligned, check single valid y
    elif align_idx1 == align_idx2 == 0:
        (x11, y11, z11), (x12, y12, z12) = brick1
        (x21, y21, z21), (x22, y22, z22) = brick2
        # same y and overlapping x intervals
        h_intersect = (y11 == y21) and ((x11 <= x21 <= x12) or (x21 <= x11 <= x22))
    # if any is y-aligned, check single valid x and overlapping y intervals
    elif align_idx1 == align_idx2 == 1:
        (x11, y11, z11), (x12, y12, z12) = brick1
        (x21, y21, z21), (x22, y22, z22) = brick2
        # same x and overlapping y intervals
        h_intersect = (x11 == x21) and ((y11 <= y21 <= y12) or (y21 <= y11 <= y22))
    else:
        raise ValueError

    return h_intersect


# sort bricks according to their minimum z coordinate
bricks = parse_file()
bottmup_bricks = sorted(bricks, key=lambda x: (min(x[1][0][2], x[1][1][2]), max(x[1][0][2], x[1][1][2])))

# start from bottom bricks and evolve to the minimum possible z (maximum possible z already occupied + 1)
brick_sustaining = {}
brick_sustained_by = {}
evolved_bricks = []
for c_idx, curr_brick in bottmup_bricks:
    (x1, y1, z1), (x2, y2, z2) = curr_brick
    curr_min_z = min(z1, z2)
    evolved_bricks_below = [b for b in evolved_bricks if curr_min_z > max(b[1][0][2], b[1][1][2])]

    # find max possible z after drop
    ev_brick_max_z = 0
    tmp_sustaining = []
    for ev_idx, ev_brick in evolved_bricks_below:
        if bricks_h_intersect(ev_brick, curr_brick):
            tmp_ev_brick_max_z = max(ev_brick[0][2], ev_brick[1][2])
            ev_brick_max_z = max(tmp_ev_brick_max_z, ev_brick_max_z)
            tmp_sustaining.append((tmp_ev_brick_max_z, ev_idx))

    # for all the candidates sustaining, get only the highest ones
    for tmp_ev_brick_max_z, ev_idx in tmp_sustaining:
        if tmp_ev_brick_max_z == ev_brick_max_z:
            # update sustained bricks
            if c_idx not in brick_sustained_by:
                brick_sustained_by[c_idx] = []
            brick_sustained_by[c_idx].append(ev_idx)

            # update sustaining bricks
            if ev_idx not in brick_sustaining:
                brick_sustaining[ev_idx] = []
            brick_sustaining[ev_idx].append(c_idx)

    # evolve brick
    max_z = ev_brick_max_z + 1
    delta_z = curr_min_z - max_z
    curr_ev_brick = ((x1, y1, z1-delta_z), (x2, y2, z2-delta_z))
    evolved_bricks.append((c_idx, curr_ev_brick))

debug = False

if debug:
    brick_sustaining = {}
    brick_sustained_by = {}
    evolved_again_bricks = []
    for c_idx, curr_brick in evolved_bricks:
        (x1, y1, z1), (x2, y2, z2) = curr_brick
        curr_min_z = min(z1, z2)
        evolved_bricks_below = [b for b in evolved_bricks if curr_min_z > max(b[1][0][2], b[1][1][2])]

        # find max possible z after drop
        ev_brick_max_z = 0
        tmp_sustaining = []
        for ev_idx, ev_brick in evolved_bricks_below:
            if bricks_h_intersect(ev_brick, curr_brick):
                tmp_ev_brick_max_z = max(ev_brick[0][2], ev_brick[1][2])
                ev_brick_max_z = max(tmp_ev_brick_max_z, ev_brick_max_z)
                tmp_sustaining.append((tmp_ev_brick_max_z, ev_idx))

        # for all the candidates sustaining, get only the highest ones
        for tmp_ev_brick_max_z, ev_idx in tmp_sustaining:
            if tmp_ev_brick_max_z == ev_brick_max_z:
                # update sustained bricks
                if c_idx not in brick_sustained_by:
                    brick_sustained_by[c_idx] = []
                brick_sustained_by[c_idx].append(ev_idx)

                # update sustaining bricks
                if ev_idx not in brick_sustaining:
                    brick_sustaining[ev_idx] = []
                brick_sustaining[ev_idx].append(c_idx)

        # evolve brick
        max_z = ev_brick_max_z + 1
        delta_z = max_z - curr_min_z
        curr_ev_brick = ((x1, y1, z1-delta_z), (x2, y2, z2-delta_z))
        evolved_again_bricks.append((c_idx, curr_ev_brick))

    assert tuple(evolved_bricks) == tuple(evolved_again_bricks)

ok_remove = []
fallen_count = []
for idx in range(len(evolved_bricks)):
    # if not sustaining, add 1
    if idx not in brick_sustaining:
        ok_remove.append(idx)
    # if sustaining but all sustained bricks have more than 1 sustain, add 1
    elif all(len(set(brick_sustained_by[s_idx])) > 1 for s_idx in brick_sustaining[idx]):
        ok_remove.append(idx)
    else:
        # not ok to remove. calculate how many would fall
        tmp_fallen = {idx}
        sustained_bricks = brick_sustaining[idx]
        while sustained_bricks:
            next_sustained_bricks = set()
            for s_idx in sustained_bricks:
                # if no more bricks would sustain it, add it to fallen and add the ones sustained by it for a check
                if not set(brick_sustained_by[s_idx]) - tmp_fallen:
                    tmp_fallen.add(s_idx)
                    next_sustained_bricks.update(brick_sustaining.get(s_idx, []))
            sustained_bricks = next_sustained_bricks

        # exclude the single one from the fallen and count
        if len(tmp_fallen) - 1 != 0:
            fallen_count.append(len(tmp_fallen) - 1)

print(len(ok_remove))
print(sum(fallen_count))

if __name__ == "__main__":
    pass
