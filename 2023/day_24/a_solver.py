

def parse_input():
    with open("a_input.txt") as f:
        input_txt = f.read()

    hailstones = []
    for e_str in input_txt.splitlines():
        p_str, v_str = e_str.split(" @ ")
        px0, py0, pz0 = map(int, p_str.split(", "))
        vx0, vy0, vz0 = map(int, v_str.split(", "))
        hailstones.append(((px0, py0, pz0), (vx0, vy0, vz0)))

    return hailstones


MIN_X_TEST = MIN_Y_TEST = 200000000000000
MAX_X_TEST = MAX_Y_TEST = 400000000000000

def find_intersection(p1, v1, p2, v2, with_z=False):
    # ax+by+cz+q = 0, where coefficients are velocities
    px1, py1, pz1 = p1
    px2, py2, pz2 = p2
    vx1, vy1, vz1 = v1
    vx2, vy2, vz2 = v2

    if not with_z:
        # ax + bx + q = 0
        # a = vy, b= - vx, q = (-x0*vy + y0*vx)
        a1 = vy1
        a2 = vy2
        b1 = - vx1
        b2 = - vx2
        q1 = (-px1*vy1 + py1*vx1)
        q2 = (-px2*vy2 + py2*vx2)

        try:
            x_inters = (q1 * b2 - q2 * b1) / (b1 * a2 - b2 * a1)
            y_inters = (q1 * a2 - q2 * a1) / (a1 * b2 - a2 * b1)
            return (x_inters, y_inters)
        except ZeroDivisionError:
            return None

    else:
        # ax+by+cz+q = 0, where coefficients are velocities
        q1 = - vx1 * px1 - vy1 * py1 - vz1 * pz1
        q2 = - vx2 * px2 - vy2 * py2 - vz2 * pz2
        try:
            x_inters = (vy1 * q2 - vy2 * q1) / (vy2 * vx1 - vy1 * vx2)
            y_inters = (vx1 * q2 - vx2 * q1) / (vx2 * vy1 - vx1 * vy2)
            return (x_inters, y_inters)
        except ZeroDivisionError:
            return None

hailstones = parse_input()
intersecting = []
for h1_idx, h1 in enumerate(hailstones):
    for delta, h2 in enumerate(hailstones[h1_idx+1:]):
        h2_idx = h1_idx + delta + 1
        p1, v1 = h1
        p2, v2 = h2
        p_inters = find_intersection(p1, v1, p2, v2, with_z=False)

        # if intersection, check that evolution forward in time (velocity and pos diff are same sign)
        if p_inters and (v1[0] * (p_inters[0] - p1[0]) >= 0) and (v2[0] * (p_inters[0] - p2[0]) >= 0):
            if ((MIN_X_TEST <= p_inters[0] <= MAX_X_TEST)
                    and (MIN_Y_TEST <= p_inters[1] <= MAX_Y_TEST)):
                intersecting.append((h1_idx, h2_idx))

if __name__ == "__main__":
    print(len(intersecting))
    pass
