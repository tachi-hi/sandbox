#!/usr/bin/env python

from matplotlib import pyplot
import numpy

def basic():
	""" Hellow World """
	pyplot.plot([1,2,1,2])
	pyplot.show() # Show the plot.


def testTeX():
	""" Use TeX command """
	pyplot.text(0,0,"$p = \\frac{1}{Z}\\exp{-\\beta H}$") # TeX commands can be used in the texts.
	pyplot.show()


def plotMyFunction(arg):
	""" Plot a function """
	pyplot.xlabel("$x$ axis")
	pyplot.ylabel("$y$ axis")
	pyplot.title("$f(x) = x^3 - x + 1$")
	pyplot.text(0, 0, "$y = f(x)$")

	if(arg == 1):
		x = numpy.arange(-2, 2, 0.1)
		f = numpy.poly1d([1, 0, -1, 1]) # f(x) = x^3 - x + 1
		y = [f(_) for _ in x]

	# or, equivalently,
	if(arg == 2):
		x = numpy.arange(-2, 2, 0.1)
		f = numpy.poly1d([1, 0, -1, 1]) # f(x) = x^3 - x + 1
		y = map(f, x)

	# or, equivalently,
	if(arg == 3):
		x = numpy.arange(-2, 2, 0.1)
		y = [(lambda v: v**3 - v + 1)(_) for _ in x]

	# or, equivalently,
	if(arg == 4):
		x = numpy.arange(-2, 2, 0.1)
		y = map(lambda v: v**3 - v + 1, x)

	pyplot.plot(x, y)
	pyplot.savefig("sample.svg", format="svg") # Save the plot instead of showing it
	pyplot.savefig("sample.eps")
	pyplot.savefig("sample.png")
	pyplot.savefig("sample.pdf")
	


