#!/usr/bin/env python

def func(a, (b, c), *args, **kwargs) : #, **kwargs):
    ret = {}
    ret["a"] = a
    ret["b"] = b
    ret["c"] = c
    for i, x in enumerate(args):
        ret[i] = x
    for k, v in kwargs.items():
        ret[k] = v
    return ret

def func2(a, (b, c), **kwargs):
    ret = {}
    ret["a"] = a
    ret["b"] = b
    ret["c"] = c
    for k, v in kwargs.items():
        ret[k] = v
    return ret


""" call func (variadic function) """
r = func("x", ("y", "z"), "d", "e", "f", A="A", B="B", C="C")
print "\n".join([ "r[" + str(k) + "]=" + str(v) for k, v in sorted(r.items()) ] )
print "\n"

""" asterisk argument"""
x = ["x", ("y", "z")]
r = func(*x)
print "\n".join([ "r[" + str(k) + "]=" + str(v) for k, v in sorted(r.items()) ] )
print "\n"

""" invalid syntax """
#    r = func(*x,"d")

""" valid """
r = func2(*x, A="A")
print "\n".join([ "r[" + str(k) + "]=" + str(v) for k, v in sorted(r.items()) ] )
print "\n"
