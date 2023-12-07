
from collections import Counter

with open('a_input.txt') as f:
    input_txt = f.read()

card_value_map = dict(zip("AKQT98765432J", range(13)[::-1]))
joker_value = card_value_map["J"]
hands = [e.split() for e in input_txt.splitlines()]

hands_sorting_tuples_v1 = []
for hand_cards, hand_bid in hands:
    hand_cards_mapped = [card_value_map[c] for c in hand_cards]
    cards_counter_map = Counter(hand_cards_mapped)
    cards_counter = cards_counter_map.most_common()
    if len(cards_counter) < 3:
        cards_counter.extend([(-1, 0), (-2, 0)])

    cards_counter_wo_joker = [e for e in cards_counter if e[0] != joker_value]
    joker_cnt = cards_counter_map[joker_value]

    top1_card_cnt = cards_counter_wo_joker[0][1] + joker_cnt
    top2_card_cnt = cards_counter_wo_joker[1][1]

    hand_sorting_tuple_v1 = tuple([top1_card_cnt, top2_card_cnt] + hand_cards_mapped)
    hands_sorting_tuples_v1.append((hand_sorting_tuple_v1, hand_bid, hand_cards))


# ######## Part 2
sorted_hands = sorted(hands_sorting_tuples_v1, key=lambda x: x[0])
sorted_bids = [(rank, int(bid)) for rank, (_, bid, _) in enumerate(sorted_hands, 1)]
score = sum([r*b for r, b in sorted_bids])

print(score)

if __name__ == "__main__":
    pass
