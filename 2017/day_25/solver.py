
import collections



def solve_pt1():
    state = "A"
    cursor = 0
    tape = collections.defaultdict(lambda: 0)
    for _ in range(12861455):
        if state == "A":
          if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
            state = "B"
          elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor -= 1
            state = "B"
        
        elif state == "B":
          if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = "C"
          elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor += 1
            state = "E"
        
        elif state == "C":
          if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
            state = "E"
          elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor -= 1
            state = "D"
        
        elif state == "D":
          if tape[cursor] == 0:
            tape[cursor] = 1
            cursor -= 1
            state = "A"
          elif tape[cursor] == 1:
            tape[cursor] = 1
            cursor -= 1
            state = "A"
        
        elif state == "E":
          if tape[cursor] == 0:
            tape[cursor] = 0
            cursor += 1
            state = "A"
          elif tape[cursor] == 1:
            tape[cursor] = 0
            cursor += 1
            state = "F"
        
        elif state == "F":
          if tape[cursor] == 0:
            tape[cursor] = 1
            cursor += 1
            state = "E"
          elif tape[cursor] == 1:
            tape[cursor] = 1
            cursor += 1
            state = "A"
    return sum(tape.values())


# ######## PART 1
score = solve_pt1()
print("Part 1 solution: ", score)


if __name__ == "__main__":
    pass