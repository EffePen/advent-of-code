
import os
import itertools
from functools import cache


def parse_input():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
        input_txt = f.read()
    lines = input_txt.splitlines()
    starting_beam_pos = 0j + lines[0].index("S")
    splitter_positions = [[e_idx + 1j*l_idx for e_idx, e in enumerate(l) if e != "."] for l_idx, l in enumerate(lines)]
    
    return starting_beam_pos, splitter_positions


def solve_pt1(starting_beam_pos, splitter_positions):
    score = 0
    beams = {starting_beam_pos}
    for splitters_pos in splitter_positions[1:]:
        new_beams = set([b+1j for b in beams])
        splitters_hit = new_beams & set(splitters_pos)
        score += len(splitters_hit)
        new_beams -= splitters_hit
        new_beams.update({b+1 for b in splitters_hit})
        new_beams.update({b-1 for b in splitters_hit})
        beams = new_beams
    return score


def solve_pt2(starting_beam_pos, splitter_positions):
    score = 0
    
    all_splitter_positions = list(itertools.chain.from_iterable(splitter_positions))

    @cache
    def get_num_paths(splitter_pos):
        num_new_paths = 1
        following_l_splitters = [s_pos for s_pos in all_splitter_positions 
                                 if s_pos.real == splitter_pos.real - 1 and s_pos.imag > splitter_pos.imag]
        following_r_splitters = [s_pos for s_pos in all_splitter_positions 
                                 if s_pos.real == splitter_pos.real + 1 and s_pos.imag > splitter_pos.imag]
        
        if following_l_splitters:
            next_l = min(following_l_splitters, key=lambda x: x.imag)
            num_new_paths += get_num_paths(next_l)
        if following_r_splitters:
            next_r = min(following_r_splitters, key=lambda x: x.imag)
            num_new_paths += get_num_paths(next_r)
        return num_new_paths
        
    starting_splitter = min([s_pos for s_pos in all_splitter_positions if s_pos.real == starting_beam_pos.real], key=lambda x: x.imag)
    score = 1 + get_num_paths(starting_splitter)

    return score


# PARSE INPUT
starting_beam_pos, splitter_positions = parse_input()

# PART 1
score = solve_pt1(starting_beam_pos, splitter_positions)
print(f"Part 1 solution: {score}")

# PART 2
score = solve_pt2(starting_beam_pos, splitter_positions)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass