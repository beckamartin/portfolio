from itertools import permutations as pm

def permutations(s):
    return sorted(set([''.join(i) for i in list(pm(s, len(s)))]))