
import re

with open('a_input.txt') as f:
    input_txt = f.read()

cmd_lines = input_txt.splitlines()

parent_dir = ["/"]
dir_files = {}

for cmd_line in cmd_lines:
    listed_dir = ""
    if cmd_line == "$ cd /":
        parent_dir = ["/"]
    elif cmd_line == "$ cd ..":
        parent_dir.pop()
    elif cmd_line.startswith("$ cd "):
        next_dir_name = cmd_line.replace("$ cd ", "")
        parent_dir.append(next_dir_name)
    elif cmd_line.startswith("$ ls"):
        pass
    elif cmd_line.startswith("dir "):
        listed_dir = cmd_line.replace("dir ", "")
    else:
        current_dir = parent_dir + [listed_dir]
        filesize_str, filename = cmd_line.split()
        filepath = "/".join(current_dir + [filename])
        filesize = int(filesize_str)

        for idx in range(len(current_dir)):
            dir_id = tuple(current_dir[:idx])
            if dir_id not in dir_files:
                dir_files[dir_id] = []

            dir_files[dir_id].append((filepath, filesize))

score = 0
for dir_id in dir_files:
    dir_filesizes = [s for fp, s in dir_files[dir_id]]
    dir_size = sum(dir_filesizes)
    if dir_size <= 100000:
        score += dir_size

print(score)



if __name__ == "__main__":
    pass
