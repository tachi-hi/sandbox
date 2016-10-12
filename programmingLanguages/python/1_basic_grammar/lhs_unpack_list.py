def fun(x):
    return [x, x*2, x*3]

# valid
[x, y, z] = fun(3)

print (x)
print (y)
print (z)

# vaild
x, y, z = fun(3)
print (x)
print (y)
print (z)

# invalid 
x, y = fun(3)
print (x)
print (y)

# valid
_, _, z = fun(3)
print(z)
