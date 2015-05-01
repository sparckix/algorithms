__author__ = 'sparckix'

''' Implementation of an instance (n=5) of the Stable Matching algorithm problem using lists and arrays.
    Problem: Given two sets (men and women), and a 2n preference list (one for each woman and man), find a stable
    matching where each man marries his best valid woman.

    The algorithm can be shown to be in the order of O(n^2)'''

# Two preference lists: one for man and one for woman. - hardcoded
from collections import OrderedDict
manPref = OrderedDict()
womanPref = OrderedDict()
manPref[0] = [0,2,3,1,4]
manPref[1] = [1,3,0,4,2]
manPref[2] = [1,4,3,0,2]
manPref[3] = [2,3,4,0,1]
manPref[4] = [3,2,4,1,0]
womanPref[0] = [0,3,2,1,4]
womanPref[1] = [3,0,4,2,1]
womanPref[2] = [2,4,1,0,3]
womanPref[3] = [1,3,4,0,2]
womanPref[4] = [3,2,4,1,0]

# current man with whom a woman is married -- used by women. Initially null (-1) for all women
current = [-1,-1,-1,-1,-1]
# List of persons to be proposed next -- used by men. Initially 0 (first woman for each list)
next = [0,0,0,0,0]
# "Linked list" used to maintain the set of free men. Initially, every men is free
free = [0,1,2,3,4]
# n represents the number of length of the set of man (and woman) - hardcoded
n = 5

while free:
    man = free.pop()
    if next[man] > n-1:
        print "error, no more woman to whom man " + str(man) + " can propose."
        exit(1)
    chosen_woman = manPref[man][next[man]]
    next[man] += 1

    if current[chosen_woman] == -1:
        current[chosen_woman] = man
    elif womanPref[chosen_woman].index(current[chosen_woman]) > womanPref[chosen_woman].index(man):
        free.append(man)
    else:
        free.append(current[chosen_woman])
        current[chosen_woman] = man

for idx, value in enumerate(current):
    print "Man " + str(value)  + " is matched with Woman " + str(idx)

