"""
    This python program demonstrates the implementation of the tuple data type.
"""

t = (1, 3, 4)
print(type(t))

t2 = (1, )
print(type(t2))

# indexing:
print(t[1])
print(t[-1])


# slicing:
print(t[::1])
print(t[:1])

# tuple assignment:
x, y, z = (10, 20, 30)

print(f"{x = }, {y = }, {z = }")

a, b= x, y

print(f"{a = }, {b = }")


a, b = b, a


print(f"{a = }, {b = }")
