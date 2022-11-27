import sys
import math
from itertools import permutations

# longest common substring, dynamic programming approach
def lcs(s1: str, s2: str) -> str:

    if len(s1) <= len(s2):  big, small = s2, s1
    else:                   big, small = s1, s2

    mem = []

    # fill initial data, 1 charatcter long matches
    for ind_b in range(len(big)):
        if small[0] == big[ind_b]:  mem.append((0, ind_b, 0))
    for ind_s in range(len(small)):
        if small[ind_s] == big[0]:  mem.append((ind_s, 0, 0))

    # no possible overlap
    if len(mem) == 0:   return s1 + s2

    longest = None
    extention_possible = True
    
    # searching for longer common substrings by checking extentions of known options
    while extention_possible:

        extention_possible = False
        option_ind = 0
        while option_ind < len(mem):

            ind_s, ind_b, old_len = mem[option_ind]
            new_len = old_len +1 # trying to extend

            if ind_s + new_len < len(small) and ind_b  + new_len < len(big):
                if small[ind_s + new_len] == big[ind_b + new_len]:

                    mem.append((ind_s, ind_b, new_len))
                    extention_possible = True

                mem.pop(option_ind) # wether it was extended or disqualified we dont want it anymore

            else:   option_ind += 1


    if len(mem) != 0:   longest = max(mem, key = lambda option : option[2]) # by length
    # no possible overlap
    else:   return s1 + s2

    # return nesting concatination
    ind_s, ind_b, ln = longest

    if ind_b == 0:
        # comlete overlap
        if ind_s == 0:  return big
        # exedes from the left
        return small[: ind_s] + big

    if ind_s == 0:
        # complete overlap
        if ind_b + len(small) -1 < len(big):  return big
        # exedes from the right
        return big[: ind_b] + small


# devide & conqure to find shortest nesting concatination of list of strings
def best_overlap(l: list) -> str:

    if len(l) == 1: return l[0]

    middle = len(l) // 2

    return lcs(best_overlap(l[:middle]), best_overlap(l[middle:]))



sequnces = []

n = int(input())
for i in range(n):
    subseq = input()
    sequnces.append(subseq)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(min([len(best_overlap(perm)) for perm in permutations(sequnces)]))