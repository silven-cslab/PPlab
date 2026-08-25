"""
    This python program shows the implementation of the minmax function.
"""

def MinMax(LIST):
    return min(LIST), max(LIST)

L = [12, 24, 1,3, 13, 45]

m, n = MinMax(L)
print(f"{m = }, {n = }")
