
import re


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()

    my_hp = 100
    enemy_stats = {l.split(": ")[0]: int(l.split(": ")[1]) for l in input_txt.splitlines()}

    weapons = {
        "Dagger": {"cost": 8, "damage": 4, "armor": 0},
        "Shortsword": {"cost": 10, "damage": 5, "armor": 0},
        "Warhammer": {"cost": 25, "damage": 6, "armor": 0},
        "Longsword": {"cost": 40, "damage": 7, "armor": 0},
        "Greataxe": {"cost": 74, "damage": 8, "armor": 0},
    }

    armors = {
        "Leather": {"cost": 13, "damage": 0, "armor": 1},
        "Chainmail": {"cost": 31, "damage": 0, "armor": 2},
        "Splintmail": {"cost": 53, "damage": 0, "armor": 3},
        "Bandedmail": {"cost": 75, "damage": 0, "armor": 4},
        "Platemail": {"cost": 102, "damage": 0, "armor": 5},
    }

    rings = {
        "Damage_1": {"cost": 25, "damage": 1, "armor": 0},
        "Damage_2": {"cost": 50, "damage": 2, "armor": 0},
        "Damage_3": {"cost": 100, "damage": 3, "armor": 0},
        "Defense_1": {"cost": 20, "damage": 0, "armor": 1},
        "Defense_2": {"cost": 40, "damage": 0, "armor": 2},
        "Defense_3": {"cost": 80, "damage": 0, "armor": 3},
    }
    return my_hp, enemy_stats, weapons, armors, rings


def part12(my_hp, enemy_stats, weapons, armors, rings):
    # to win we need:
    # (my_damage - enemy_armour) >= (enemy_damage - my_armour) + ceil(hp_diff / n_rounds)
    # => (8 + 2) = (enemy_damage + enemy_armour) <= (my_damage + my_armour)
    min_win = None
    max_defeat = None
    for wid, w_dict in weapons.items():
        w_damage = w_dict["damage"]
        w_armor = w_dict["armor"]
        w_cost = w_dict["cost"]
        
        for aid in [None] + list(armors.keys()):
            a_damage = armors[aid]["damage"] if aid is not None else 0
            a_armor = armors[aid]["armor"] if aid is not None else 0
            a_cost = armors[aid]["cost"] if aid is not None else 0

            for rid1 in [None] + list(rings.keys()):
                r1_damage = rings[rid1]["damage"] if rid1 is not None else 0
                r1_armor = rings[rid1]["armor"] if rid1 is not None else 0
                r1_cost = rings[rid1]["cost"] if rid1 is not None else 0
            
                for rid2 in [None] + list(rings.keys()):
                    rid2 = rid2 if rid1 != rid2 else None
                    r2_damage = rings[rid2]["damage"] if rid2 is not None else 0
                    r2_armor = rings[rid2]["armor"] if rid2 is not None else 0
                    r2_cost = rings[rid2]["cost"] if rid2 is not None else 0
                    
                    my_tot_damage = w_damage + a_damage + r1_damage + r2_damage
                    my_tot_armor = w_armor + a_armor + r1_armor + r2_armor
                    my_tot_cost = w_cost + a_cost + r1_cost + r2_cost

                    tmp_my_hp = my_hp
                    tmp_enemy_hp = enemy_stats["Hit Points"]
                    while tmp_my_hp >= 0 and tmp_enemy_hp >= 0:
                        tmp_my_hp -= max(1, enemy_stats["Damage"] - my_tot_armor)
                        tmp_enemy_hp -= max(1, my_tot_damage - enemy_stats["Armor"])

                    if tmp_enemy_hp <= 0:
                        if not min_win or my_tot_cost < min_win[0]:
                            min_win = (my_tot_cost, my_tot_damage + my_tot_armor, [wid, aid, rid1, rid2])
                    else:
                        if not max_defeat or my_tot_cost > max_defeat[0]:
                            max_defeat = (my_tot_cost, my_tot_damage + my_tot_armor, [wid, aid, rid1, rid2])
    return min_win, max_defeat


# input
my_hp, enemy_stats, weapons, armors, rings = parse_input()

# part 1 & 2
min_win, max_defeat = part12(my_hp, enemy_stats, weapons, armors, rings)

# part 1
print("Part 1:", min_win[0])

# part 2
print("Part 2:", max_defeat[0])


if __name__ == "__main__":
    pass
