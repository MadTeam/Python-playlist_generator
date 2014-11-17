#!/usr/bin/python3

def additionAbs(a, b):
	'''
	>>> additionAbs(2,3)
	5
	>>> additionAbs(2,-3)
	5
	'''
	return a + b

print(additionAbs(2, -3))

import doctest
doctest.testmod()
