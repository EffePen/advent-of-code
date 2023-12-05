
import re
import random

with open('a_input.txt') as f:
    input_txt = f.read()

items_map = dict(zip(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), range(1, 53)))

elf_sacks = input_txt.splitlines()
elf_teams_num = len(elf_sacks) // 3
common_items = []
for idx in range(elf_teams_num):
    elf1, elf2, elf3 = elf_sacks[idx*3:(idx+1)*3]

    common_item, = set(list(elf1)) & set(list(elf2)) & set(list(elf3))
    common_items.append(common_item)

print(common_items)
print(sum(items_map[i] for i in common_items))

if __name__ == '__main__':
    pass