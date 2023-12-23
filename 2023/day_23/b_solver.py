import functools
import os
import time


def parse_file():
    with open("a_input.txt") as f:
        input_txt = f.read()

    map = input_txt.splitlines()
    return map


@functools.lru_cache(maxsize=None)
def get_next_moves(slice, relative_pos):
    tot_possible_moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    # get only possible ones
    possible_moves = set()
    r_idx, c_idx = relative_pos
    for mv in tot_possible_moves:
        dr, dc = mv
        nr_idx = r_idx + dr
        nc_idx = c_idx + dc
        try:
            nblock = slice[nr_idx][nc_idx]
        except IndexError:
            continue

        if nblock == "." or nblock in ("<", ">", "v", "^"):
            possible_moves.add(mv)
        elif nblock == "#":
            continue
        else:
            raise ValueError
    return possible_moves


map = parse_file()
n_rows = len(map)
n_cols = len(map[0])
start_pos = (0, map[0].index("."))
end_pos = (n_rows-1, map[-1].index("."))
first_move = [1, 0]
curr_pos = (start_pos[0] + first_move[0], start_pos[1] + first_move[1])
trail_id = (0,)
curr_positions_prev_moves = [(curr_pos, first_move, trail_id)]
trail_parts = {trail_id: [curr_pos]}

debug = False

longest_path_len = 0
step_idx = 0
while curr_positions_prev_moves:
    if debug:
        viz_map = [r for r in map]
        for (dbr_idx, dbc_idx), _ in curr_positions_prev_moves:
            viz_map[dbr_idx] = viz_map[dbr_idx][:dbc_idx] + "S" + viz_map[dbr_idx][dbc_idx+1:]
        print("\n".join(viz_map))
        time.sleep(1)

    step_idx += 1
    next_positions_curr_moves = []
    for curr_pos, prev_move, curr_trail_id in curr_positions_prev_moves:
        r_idx, c_idx = curr_pos
        rs_idx = max(r_idx - 1, 0)
        re_idx = min(r_idx + 2, n_rows)
        cs_idx = max(c_idx - 1, 0)
        ce_idx = min(c_idx + 2, n_cols)
        relative_pos = (r_idx - rs_idx, c_idx - cs_idx)

        slice = tuple(r[cs_idx:ce_idx] for r in map[rs_idx:re_idx])
        # get possible next moves (and remove last reversed one, if present)
        next_moves = get_next_moves(slice, relative_pos) - {(- prev_move[0], - prev_move[1])}
        a = 1
        for mv_idx, mv in enumerate(next_moves):
            next_pos = (curr_pos[0] + mv[0], curr_pos[1] + mv[1])

            # if the trail forks, update trail idx for each next position
            if len(next_moves) == 1:
                next_trail_id = curr_trail_id
            else:
                next_trail_id = tuple(list(curr_trail_id) + [mv_idx])
                if next_trail_id not in trail_parts:
                    trail_parts[next_trail_id] = []

                # check that the curr pos is not in any previous trail parts of current trail
                skip = False
                for subs_len in range(1, len(next_trail_id) - 1):
                    prev_trail_id = tuple(list(next_trail_id)[:subs_len])
                    if next_pos in trail_parts[prev_trail_id]:
                        skip = True
                        break
                if skip:
                    break

            # update trail positions
            trail_parts[next_trail_id].append(next_pos)

            # if next pos is the last one, save longest path len
            if next_pos == end_pos:
                longest_path_len = step_idx
                print(longest_path_len + 1)
            next_positions_curr_moves.append((next_pos, mv, next_trail_id))
    curr_positions_prev_moves = next_positions_curr_moves
    #print(curr_positions_prev_moves)

print(longest_path_len + 1)


if __name__ == "__main__":
    pass
