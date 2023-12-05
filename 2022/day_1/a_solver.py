
import re
import random

with open('a_input.txt') as f:
    input_txt = f.read()


elf_items = [[int(e) for e in elf_txt.splitlines()] for elf_txt in input_txt.split("\n\n")]
elf_calories = [sum(items) for items in elf_items]
print(max(elf_calories))

print(sum(sorted(elf_calories, reverse=True)[:3]))


if __name__ == '__main__':
    pass