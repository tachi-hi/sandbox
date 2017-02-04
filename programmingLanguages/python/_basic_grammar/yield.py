

def func():
    for i in range(10):
        yield i

def g():
    j = 0
    while True:
        yield j
        j += 1

# generator
gen = g()
for i in range(20):
    tmp = gen.next()
    print(tmp)

# infinte loop using iterator
for i, g_ in enumerate(g()):
    print(g_)
    if i > 100:
        break

# stop iterator
gen = func()
for i in range(20):
    tmp = gen.next()
    print(tmp)


