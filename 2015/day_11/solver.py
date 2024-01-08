


# find the rightmost letter that MUST be changed in order to:
# - allow 2 non overlapping consecutive identical pairs
# - allow 3 consecutive letters

# Given that i,l,o cannot be used, only a->h and p->z can be used for the 3 consecutive letters
# alphabet = "abcdefgh ijklmno pqrstuvwxyz"

# note: try keeping the leftmost as low as possible to have the lowest possible number
# note: the leftmost letters do comply with any of the rules => the patterns must be created anew
# note: at least 5 letters to have 2 pairs and the 3 consecutive
input_txt = "vzbxkghb"
p1_solution = "vzbxxyzz"
p2_solution = "vzcaabcc"
