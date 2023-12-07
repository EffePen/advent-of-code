
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
            dir_id = "/".join(current_dir[:idx])
            if dir_id not in dir_files:
                dir_files[dir_id] = []

            dir_files[dir_id].append(filesize)


tot_disk_size = 70000000
needed_free_disk_size = 30000000
tot_used_space = sum(dir_files["/"])
current_free_disk_space = tot_disk_size - tot_used_space
min_data_to_delete = needed_free_disk_size - current_free_disk_space


print(min([sum(file_sizes) for file_sizes in dir_files.values()
           if sum(file_sizes) >= min_data_to_delete]))

if __name__ == "__main__":
    pass
