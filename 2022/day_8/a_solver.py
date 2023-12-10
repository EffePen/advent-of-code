

with open("a_input.txt") as f:
    input_txt = f.read()

rows = [[int(t) for t in l] for l in input_txt.splitlines()]
cols = [list(tup) for tup in list(zip(*rows))]

visible_trees = 2 * len(rows) + 2 * (len(cols) - 2)

# iterate over each tree excluding edges
for r_idx in range(1, len(rows)-1):
    for c_idx in range(1, len(cols)-1):
        curr_tree_height = rows[r_idx][c_idx]
        if all([h < curr_tree_height for h in rows[r_idx][:c_idx]]) or \
           all([h < curr_tree_height for h in rows[r_idx][c_idx+1:]]) or \
           all([h < curr_tree_height for h in cols[c_idx][:r_idx]]) or \
           all([h < curr_tree_height for h in cols[c_idx][r_idx+1:]]):
            visible_trees += 1


print(visible_trees)

# iterate over each tree
max_view = 0
for r_idx in range(len(rows)):
    for c_idx in range(len(cols)):
        curr_view = 1
        curr_tree_height = rows[r_idx][c_idx]

        hl_trees = rows[r_idx][:c_idx]
        hr_trees = rows[r_idx][c_idx + 1:]
        vu_trees = cols[c_idx][:r_idx]
        vd_trees = cols[c_idx][r_idx + 1:]

        curr_scores = []
        for tree_range in [hl_trees[::-1], vu_trees[::-1], hr_trees, vd_trees]:
            curr_score = 0
            for tree_h in tree_range:
                curr_score += 1
                if tree_h >= curr_tree_height:
                    break
            curr_view *= curr_score

        if curr_view > max_view:
            max_view = curr_view

print(max_view)

if __name__ == "__main__":
    pass