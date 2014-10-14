#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

def powset(x):
  """
  argument: a list X
  return: list of the power set of X (2^X)
  """

    ret=[]
    for r in range(len(x) + 1):
        ret.extend(list(itertools.combinations(x, r)))
    return [list(i) for i in ret]

