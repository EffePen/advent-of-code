
import re


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()

    replacements_txt, molecule = input_txt.split("\n\n")
    replacements_dict = dict()
    rev_replacements_dict = dict()
    for l in replacements_txt.splitlines():
        elem, repl = l.split(" => ")
        if not elem in replacements_dict:
            replacements_dict[elem] = []
        replacements_dict[elem].append(repl)

        if repl not in rev_replacements_dict:
            rev_replacements_dict[repl] = []
        rev_replacements_dict[repl].append(elem)

    return molecule, replacements_dict, rev_replacements_dict


def part1(molecule, replacements_dict, n_iterations=1):
    curr_molecules = [molecule]
    for _ in range(n_iterations):
        next_molecules = []
        for curr_mol in curr_molecules:
            for elem, replacements in replacements_dict.items():
                for match in re.finditer(elem, curr_mol):
                    for repl in replacements:
                        next_mol = curr_mol[:match.start()] + repl + curr_mol[match.end():]
                        next_molecules.append(next_mol)
        curr_molecules = next_molecules
    return curr_molecules


def part2(molecule, replacements_dict):
    curr_molecules = ["e"]

    end = ["Rn", "Ar", "Y", "C"]
    n_iterations = 0
    while molecule not in curr_molecules:
        n_iterations += 1
        next_molecules = []
        for curr_mol in set(curr_molecules):
            for elem, replacements in replacements_dict.items():
                for match in re.finditer(elem, curr_mol):
                    for repl in replacements:
                        next_mol = curr_mol[:match.start()] + repl + curr_mol[match.end():]
                        if ((next_mol[0] in ("H", "O"))
                                and ("H" not in next_mol[1:])
                                and ("O" not in next_mol[1:])
                                and "C" not in next_mol.replace("Ca", "")
                        ):
                            # deve iniziare per H o per O (altrimenti non può mai evolvere con O come iniziale)
                            next_molecules.append(next_mol)
        curr_molecules = next_molecules
    return n_iterations


def part2v2(molecule, rev_replacements_dict):
    # NOTE: NOT WORKING
    final_molecule = "e"

    # reverse
    n_iterations = 0
    while final_molecule != molecule:
        for elem, replacements in rev_replacements_dict.items():
            if elem in molecule:
                for match in re.finditer(elem, molecule):
                    n_iterations += 1
                    repl, = replacements
                    next_molecule = molecule[:match.start()] + repl + molecule[match.end():]
                    molecule = next_molecule
                    break
    return n_iterations


def part2v3(molecule, rev_replacements_dict):
    # NOTE: NOT WORKING
    curr_molecules = [molecule]
    final_molecule = "e"
    n_iterations = 0
    while final_molecule not in curr_molecules:
        n_iterations += 1
        next_molecules = []
        for curr_mol in set(curr_molecules):
            for elem, replacements in rev_replacements_dict.items():
                for match in re.finditer(f"(?=({elem}))", curr_mol):
                    for repl in replacements:
                        idx1, idx2 = match.regs[1]
                        next_mol = curr_mol[:idx1] + repl + curr_mol[idx2:]
                        next_molecules.append(next_mol)
        curr_molecules = next_molecules
    return n_iterations





# input
molecule, replacements_dict, rev_replacements_dict = parse_input()

# part 1
next_molecules = part1(molecule, replacements_dict, n_iterations=1)
print("Part 1:", len(set(next_molecules)))

# part 2
#rev_replacements_items = sorted(list(rev_replacements_dict.items()), key=lambda e: len(e[0]), reverse=True)
#n_iterations = part2v2(molecule, rev_replacements_dict)
#n_iterations = transform_back(molecule, rev_replacements_items, n_iter=0)

# Had to follow https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/
print("Part 2:", 292 - 36 - 36 - 2*6 - 1)



if __name__ == "__main__":
    pass
