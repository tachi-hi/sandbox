import functools

""" Something similar to foldl.
If the operation is associative, it is simple.
If the operation is not associative, it is confusing.
"""

# simple example
def intersectionOfLists(*args):
    s = [set(a) for a in args]
    ret = functools.reduce(lambda x, y : x & y, s)
    return sorted(ret)

tmp = intersectionOfLists(
    [i for i in range(1000)],
    [i for i in range(1000) if i % 3 == 0],
    [i for i in range(1000) if i % 4 == 0],
    [i for i in range(1000) if i % 5 == 0]
)
print(tmp)

# another example (not associative)
f = lambda x, y: (x, (y, ))
tmp = functools.reduce(f, range(10))
print(tmp)

# >> (((((((((0, (1,)), (2,)), (3,)), (4,)), (5,)), (6,)), (7,)), (8,)), (9,))
# this result indicates that "reduce" is left associative.
