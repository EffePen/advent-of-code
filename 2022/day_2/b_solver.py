
import re
import random

with open('a_input.txt') as f:
    input_txt = f.read()

opponent_moves_map = {"A": "r", "B": "p", "C": "s"}
result_score_map = {"X": 0, "Y": 3, "Z": 6}
my_moves_value = {"r": 1, "p": 2, "s": 3}

game_win_sets = [("p", "s"), ("r", "p"), ("s", "r")]

score = 0
for l in input_txt.splitlines():
    game_score = 0
    o, result_val = l.split()
    o = opponent_moves_map[o]
    game_score += result_score_map[result_val]

    if result_val == "Y":
        m = o
    elif result_val == "Z":
        m, = [e[1] for e in game_win_sets if e[0] == o]
    else:
        m, = [e[0] for e in game_win_sets if e[1] == o]

    game_score += my_moves_value[m]
    score += game_score

print(score)


if __name__ == '__main__':
    pass