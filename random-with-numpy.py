import numpy as numpy

# we can generate an array of float
numpy.random.seed(0)

array_like_float = numpy.random.rand(5)
print(array_like_float)

# [0.5488135  0.71518937 0.60276338 0.54488318 0.4236548 ]

# we can generate a two-dimensional array

numpy.random.seed(0)

two_dimensional_array = numpy.random.rand(3, 5)
print(two_dimensional_array)

'''
[[0.5488135  0.71518937 0.60276338 0.54488318 0.4236548 ]
 [0.64589411 0.43758721 0.891773   0.96366276 0.38344152]
 [0.79172504 0.52889492 0.56804456 0.92559664 0.07103606]]
'''
