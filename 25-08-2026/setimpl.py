""" 
    This python program shows the implementation of the sets in the python programming language.
"""

a = set()
a.add(1)
a.add(1)

b = {2, 3}
print(a)
print(b)
print(type(a))

c = ()
print(type(c))

set1 = {1, 2, 3, 4, 5, 6}
set2 = {7, 8, 9, 0, 1, 2, 3}

set3 = set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)

set5 = set1.difference(set2)
print(set5)
