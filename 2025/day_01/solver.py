

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read().replace("R", "+").replace("L", "-")
    moves = [int(e) for e in input_txt.splitlines()]
    return moves


def solve_pt1(moves):
    pos = 50
    score = 0
    for m in moves:
        pos = (pos + m) % 100
        if pos == 0:
            score += 1
    return score


def solve_pt2(moves):
    prev_pos = 50
    score = 0
    for m in moves:
        full_turns = abs(m) // 100
        score += full_turns
        m -= (m/abs(m) * 100 * full_turns)
        moved_pos = (prev_pos + m)
        pos = moved_pos % 100
        if pos == 0 or (prev_pos != 0 and moved_pos != pos):
            score += 1
        prev_pos = pos
    return score


# PARSE INPUT
moves = parse_input()

# PART 1
score = solve_pt1(moves)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(moves)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass