
import re

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()

    return input_txt.splitlines()


# part 1
diffs = []
code_strings = parse_input()
memory_strings = []
for code_string in code_strings:
    memory_string = re.sub(r"(\\\\|\\\"|\\x[0-9a-f]{2})", "A", code_string[1:-1])
    memory_strings.append(memory_string)

code_string_lengths = list(map(len, code_strings))
memory_string_lengths = list(map(len, memory_strings))

print("Part 1:", sum(code_string_lengths) - sum(memory_string_lengths))


# part 2
diffs = []
memory_strings = parse_input()
code_strings = []
for memory_string in memory_strings:
    code_string = "\"" + memory_string.replace("\\", "\\\\").replace("\"", "\\\"") + "\""
    code_strings.append(code_string)

code_string_lengths = list(map(len, code_strings))
memory_string_lengths = list(map(len, memory_strings))

print("Part 2:", sum(code_string_lengths) - sum(memory_string_lengths))


if __name__ == "__main__":
    pass
