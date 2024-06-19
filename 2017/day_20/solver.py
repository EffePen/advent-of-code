

import math
import itertools


def parse_input():
    with open("input.txt") as f:
        particles_str = f.read().splitlines()
    particles = dict()
    for p_idx, p_str in enumerate(particles_str):
        particles[p_idx] = {}
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
    particles = sorted([(p_idx, z_index(p)) for p_idx, p in particles.items()], key=lambda x: x[1])
    return particles


# NOTE: this cannot work, since p(t) = p0 + v0*t + 0.5*a*t**2
# does not hold in this discrete setting
# The right equation is the following
#        v(t) = v0 + a0*t
#        p(t) = p0 + sum{t=1->t+1}(v0 + a0*t) =
#             = p0 + v0*t + (t+1)*t/2 * a0
#             = p0 + (v0 + a0/2)*t + 1/2*a0*t**2
def find_collision_times(p1, p2):
    dims_collision_times = []

    # for each dimension, calculate the solutions for t
    for dim in range(3):
        a = ( 0.5 * p2["a"][dim] - 0.5 * p1["a"][dim])
        b = ((0.5 * p2["a"][dim] + p2["v"][dim]) - (0.5 * p1["a"][dim] + p1["v"][dim]))
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


def solution_pt2_analytical(particles):
    # find all possible collisions between pairs of particles
    potential_collided = []
    particle_ids = list(particles.keys())
    for idx1, p1_idx in enumerate(particle_ids):
        for p2_idx in particle_ids[idx1+1:]:
            p1 = particles[p1_idx]
            p2 = particles[p2_idx]
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


def simulate_timestep(particles):
    for idx in particles.keys():
        particles[idx]["v"] = [vi + ai for vi, ai in zip(particles[idx]["v"], particles[idx]["a"])]
        particles[idx]["p"] = [pi + vi for pi, vi in zip(particles[idx]["p"], particles[idx]["v"])]
    return particles


def remove_collided(particles):
    particles_idxs = sorted([(p["p"], p_idx) for p_idx, p in particles.items()], key=lambda x: x[0])
    for p, p_group in itertools.groupby(particles_idxs, key=lambda x: x[0]):
        p_group = list(p_group)
        if len(p_group) > 1:
            for (_, p_idx) in p_group:
                particles.pop(p_idx)
    return particles


def solution_pt2_simulated(particles):
    for _ in range(5000):
        particles = remove_collided(particles)
        particles = simulate_timestep(particles)
    return particles


particles = parse_input()


# ######## PART 1
particles_index = find_closest_to_zero(particles)
print("Part 1 solution: ", particles_index[0][0])


# ######## PART 2
collided = solution_pt2_analytical(particles)
print("Part 2 solution: ", len(particles) - len(collided))
# particles = solution_pt2_simulated(particles)
# print("Part 2 solution: ", len(particles))


if __name__ == "__main__":
    pass