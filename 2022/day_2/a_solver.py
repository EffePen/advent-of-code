
import re
import random

with open('a_input.txt') as f:
    input_txt = f.read()

opponent_moves_map = {"A": "r", "B": "p", "C": "s"}
my_moves_map = {"X": "r", "Y": "p", "Z": "s"}
my_moves_value = {"r": 1, "p": 2, "s": 3}

game_win_sets = [("p", "s"), ("r", "p"), ("s", "r")]

games = [(opponent_moves_map[l.split()[0]], my_moves_map[l.split()[1]])
         for l in input_txt.splitlines()]

score = 0
for g in games:
    game_score = 0

    o, m = g
    if o == m:
        game_score += 3
    elif g in game_win_sets:
        game_score += 6

    game_score += my_moves_value[m]
    score += game_score

print(score)


if __name__ == '__main__':
    pass