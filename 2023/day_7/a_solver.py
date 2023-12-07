
from collections import Counter

with open('a_input.txt') as f:
    input_txt = f.read()

card_value_map = dict(zip("AKQJT98765432", range(13)[::-1]))
hands = [e.split() for e in input_txt.splitlines()]

hands_sorting_tuples_v1 = []
for hand_cards, hand_bid in hands:
    hand_cards_mapped = [card_value_map[c] for c in hand_cards]
    cards_counter = Counter(hand_cards_mapped).most_common()
    if len(cards_counter) == 1:
        cards_counter.append((0, 0))

    top1_card_cnt = cards_counter[0][1]
    top2_card_cnt = cards_counter[1][1]

    hand_sorting_tuple_v1 = tuple([top1_card_cnt, top2_card_cnt] + hand_cards_mapped)
    hands_sorting_tuples_v1.append((hand_sorting_tuple_v1, hand_bid, hand_cards))


# ######## Part 1
sorted_hands = sorted(hands_sorting_tuples_v1, key=lambda x: x[0])
sorted_bids = [(rank, int(bid)) for rank, (_, bid, _) in enumerate(sorted_hands, 1)]
score = sum([r*b for r, b in sorted_bids])

print(score)

if __name__ == "__main__":
    pass
