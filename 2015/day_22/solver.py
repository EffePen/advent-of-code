

import heapq


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


def apply_spell(status, spell):
    status["my_mana"] -= SPELLS_DICT[spell]["cost"]
    status["mana_spent"] += SPELLS_DICT[spell]["cost"]

    # cast spell
    if spell == "Magic Missile":
        status["enemy_hp"] -= 4
    elif spell == "Drain":
        status["enemy_hp"] -= 2
        status["my_hp"] += 2
    elif spell == "Shield":
        status["effects"] += ((spell, 6),)
    elif spell == "Poison":
        status["effects"] += ((spell, 6),)
    elif spell == "Recharge":
        status["effects"] += ((spell, 5),)
    else:
        raise ValueError

    # boss turn
    # apply effects
    my_armor = 0
    for effect, turns in status["effects"]:
        if effect == "Shield":
            my_armor += 7
        elif effect == "Poison":
            status["enemy_hp"] -= 3
        elif effect == "Recharge":
            status["my_mana"] += 101
    status["effects"] = tuple((e, et-1) for e, et in status["effects"] if et > 1)

    if status["enemy_hp"] <= 0:
        return status

    status["my_hp"] -= max(1, enemy_damage - my_armor)
    if status["my_hp"] <= 0:
        return status

    # beginning of my turn
    # apply effects
    my_armor = 0
    for effect, turns in status["effects"]:
        if effect == "Shield":
            my_armor += 7
        elif effect == "Poison":
            status["enemy_hp"] -= 3
        elif effect == "Recharge":
            status["my_mana"] += 101
    status["effects"] = tuple((e, et-1) for e, et in status["effects"] if et > 1)

    return status


def solve_pt1(my_hp, my_mana, enemy_hp, enemy_damage):
    initial_status = {
        "my_hp": my_hp,
        "my_mana": my_mana,
        "enemy_hp": enemy_hp,
        "enemy_damage": enemy_damage,
        "effects": (),
        "mana_spent": 0,
    }
    statuses = [(initial_status["mana_spent"], tuple(sorted(initial_status.items())))]
    heapq.heapify(statuses)
    seen_statuses = set()

    while True:
        mana_spent, status = heapq.heappop(statuses)
        status_dict = dict(status)
        available_spells = sorted([sk for sk, sd in SPELLS_DICT.items() if sd["cost"] <= status_dict["my_mana"]
                                  and sk not in [e for e, _ in status_dict["effects"]]],
                                  key=lambda x: SPELLS_DICT[x].get("cost", 0))
        for new_spell in available_spells:
            if (status, new_spell) in seen_statuses:
                continue

            status_dict = dict(status)
            new_status = apply_spell(status_dict, new_spell)
            new_elem = (new_status["mana_spent"], tuple(sorted(new_status.items())))
            seen_statuses.add((status, new_spell))

            if new_status["enemy_hp"] <= 0:
                return new_status["mana_spent"]
            elif new_status["my_hp"] > 0 and new_elem not in statuses:
                heapq.heappush(statuses, new_elem)


# input
my_hp, my_mana, enemy_hp, enemy_damage, SPELLS_DICT = parse_input()

# part 1
min_mana = solve_pt1(my_hp, my_mana, enemy_hp, enemy_damage)

# part 1 # 1482
print("Part 1:", min_mana)


if __name__ == "__main__":
    pass
