

lst = zip([0,0,0],[1,1,1],[2,2,2], [3,3,3])
for i in lst:
    print (i)

# (0, 1, 2, 3)
# (0, 1, 2, 3)
# (0, 1, 2, 3)

# ----------------------------------------------------
# this does not work as supposed
l = ([i] * 3 for i in range(4))
lst = zip(l)
for i in lst:
    print (i)

# ([0, 0, 0],)
# ([1, 1, 1],)
# ([2, 2, 2],)
# ([3, 3, 3],)

# ----------------------------------------------------
# unpack argument list using asterisk (*)
# tuple
l = ([i] * 3 for i in range(4))
lst = zip(*l)
for i in lst:
    print (i)

# (0, 1, 2, 3)
# (0, 1, 2, 3)
# (0, 1, 2, 3)

# ----------------------------------------------------
# tuple
lst = zip(*([i] * 3 for i in range(4)))
for i in lst:
    print (i)

# (0, 1, 2, 3)
# (0, 1, 2, 3)
# (0, 1, 2, 3)

# ----------------------------------------------------
# list
lst = zip(*[[i] * 3 for i in range(4)])
for i in lst:
    print (i)

# (0, 1, 2, 3)
# (0, 1, 2, 3)
# (0, 1, 2, 3)
