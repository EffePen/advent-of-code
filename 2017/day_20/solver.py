

import math
import itertools


def parse_input():
    with open("input.txt") as f:
        particles_str = f.read().splitlines()
    particles = []
    for p_idx, p_str in enumerate(particles_str):
        particles.append({})
        for m_str in p_str.split(", "):
            m, m_vals_str = m_str.split("=")
            particles[p_idx][m] = [int(e) for e in m_vals_str.strip("<>").split(",")]

    return particles


def z_index(particle):
    index = (
        sum(abs(e) for e in particle["a"]),
        sum(abs(e) for e in particle["v"]),
        sum(abs(e) for e in particle["p"])
    )
    return index


def find_closest_to_zero(particles):
    # the closest will be the ones with lowest total acceleration
    # then the ones with lowest initial velocity
    # then the ones with lowest initial position
    particles = sorted([(p_idx, z_index(p)) for p_idx, p in enumerate(particles)], key=lambda x: x[1])
    return particles


def find_collision_times(p1, p2):
    dims_collision_times = []

    # for each dimension, calculate the solutions for t
    for dim in range(3):
        a = (p2["a"][dim] - p1["a"][dim])
        b = (p2["v"][dim] - p1["v"][dim])
        c = (p2["p"][dim] - p1["p"][dim])
        if a != 0:
            if b != 0:
                try:
                    delta = math.sqrt(b**2 - 4*a*c)
                    t1 = (-b + delta)/(2*a)
                    t2 = (-b - delta)/(2*a)
                    dims_collision_times.append({t1, t2})
                except ValueError:
                    return set()
            else:
                try:
                    t1 = + math.sqrt(-c/a)
                    t2 = - math.sqrt(-c/a)
                    dims_collision_times.append({t1, t2})
                except ValueError:
                    return set()
        else:
            if b != 0:
                t1 = t2 = - c / b
                dims_collision_times.append({t1, t2})
            else:
                if c == 0:
                    # in this case, the position is constant and is identical
                    # for both particles along this dimension
                    continue
                else:
                    return set()

    collision_times = set.intersection(*dims_collision_times)
    return collision_times


def solution_pt2(particles):
    # find all possible collisions between pairs of particles
    potential_collided = []
    for p1_idx, p1 in enumerate(particles):
        for p2_idx, p2 in enumerate(particles[p1_idx+1:], p1_idx+1):
            collision_times = find_collision_times(p1, p2)
            for t in collision_times:
                potential_collided.extend([(t, p1_idx, p2_idx)])

    # exclude past times and sort by collision time
    potential_collided = [e for e in potential_collided if e[0] >= 0]
    potential_collided = sorted(potential_collided, key=lambda x: x[0])
    already_collided = set()
    for t, t_group in itertools.groupby(potential_collided, key=lambda x: x[0]):
        new_collided = set()
        for _, p1_idx, p2_idx in t_group:
            if not (p1_idx in already_collided or p2_idx in already_collided):
                new_collided.update([p1_idx, p2_idx])
        already_collided.update(new_collided)

    return already_collided


particles = parse_input()


# ######## PART 1
particles_index = find_closest_to_zero(particles)
print("Part 1 solution: ", particles_index[0][0])


# ######## PART 2
already_collided = solution_pt2(particles)
print("Part 1 solution: ", len(particles) - len(already_collided))


if __name__ == "__main__":
    pass