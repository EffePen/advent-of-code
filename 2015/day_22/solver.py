

import math


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()

    my_hp = 50
    my_mana = 500
    enemy_stats = {l.split(": ")[0]: int(l.split(": ")[1]) for l in input_txt.splitlines()}
    enemy_hp = enemy_stats["Hit Points"]
    enemy_damage = enemy_stats["Damage"]

    spells_dict = {
        "Magic Missile": {"cost": 53, "damage": 4},
        "Drain": {"cost": 73, "damage": 2, "hp": 2},
        "Shield": {"cost": 113, "armor": 7, "turns": 6},
        "Poison": {"cost": 173, "damage": 3, "turns": 6},
        "Recharge": {"cost": 229, "mana": 101, "turns": 5},
    }

    return my_hp, my_mana, enemy_hp, enemy_damage, spells_dict


MAX_MANA_SPENT = math.inf


def evolve(spells, my_hp, my_mana, enemy_hp, enemy_damage, effects, mana_spent):
    global MAX_MANA_SPENT
    if mana_spent > MAX_MANA_SPENT:
        return math.inf

    spell = spells[-1]
    # cast spell
    if spell == "Magic Missile":
        enemy_hp -= 4
    elif spell == "Drain":
        enemy_hp -= 2
        my_hp += 2
    elif spell == "Shield":
        effects.append((spell, 6))
    elif spell == "Poison":
        effects.append((spell, 6))
    elif spell == "Recharge":
        effects.append((spell, 5))
    else:
        raise ValueError

    # boss turn
    # apply effects
    my_armor = 0
    for effect, turns in effects:
        if effect == "Shield":
            my_armor += 7
        elif effect == "Poison":
            enemy_hp -= 3
        elif effect == "Recharge":
            my_mana += 101
    effects = [(e, et-1) for e, et in effects if et > 1]

    if enemy_hp <= 0:
        MAX_MANA_SPENT = mana_spent
        return mana_spent
    else:
        my_hp -= max(1, enemy_damage - my_armor)
        if my_hp <= 0:
            return math.inf

    # my turn
    my_armor = 0
    for effect, turns in effects:
        if effect == "Shield":
            my_armor += 7
        elif effect == "Poison":
            enemy_hp -= 3
        elif effect == "Recharge":
            my_mana += 101
    effects = [(e, et - 1) for e, et in effects if et > 1]

    if enemy_hp <= 0:
        return mana_spent

    # try available spells
    available_spells = sorted([sk for sk, sd in SPELLS_DICT.items() if sd["cost"] <= my_mana], key=lambda x: SPELLS_DICT[x]["cost"])
    if not available_spells:
        return math.inf
    else:
        return min(evolve(spells=spells + [new_spell],
                          my_hp=my_hp,
                          my_mana=my_mana - SPELLS_DICT[new_spell]["cost"],
                          enemy_hp=enemy_hp,
                          enemy_damage=enemy_damage,
                          effects=effects,
                          mana_spent=mana_spent + SPELLS_DICT[new_spell]["cost"])
                   for new_spell in available_spells)


def solve_pt1(my_hp, my_mana, enemy_hp, enemy_damage):
    available_spells = sorted([sk for sk, sd in SPELLS_DICT.items() if sd["cost"] <= my_mana], key=lambda x: SPELLS_DICT[x]["cost"])
    return min(evolve(spells=[new_spell],
                      my_hp=my_hp,
                      my_mana=my_mana - SPELLS_DICT[new_spell]["cost"],
                      enemy_hp=enemy_hp,
                      enemy_damage=enemy_damage,
                      effects=[],
                      mana_spent=SPELLS_DICT[new_spell]["cost"])
               for new_spell in available_spells)


# input
my_hp, my_mana, enemy_hp, enemy_damage, SPELLS_DICT = parse_input()

# part 1
min_mana = solve_pt1(my_hp, my_mana, enemy_hp, enemy_damage)

# part 1
print("Part 1:", min_mana)


if __name__ == "__main__":
    pass
