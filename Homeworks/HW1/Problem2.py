"""Problem 2: Matrix inversion via libraries and research
Write a code that can invert a given matrix,using as much pre-existing
code as possible. Through legal use of numerical libraries/packages, see
how little code you have to write yourself to do this task (we'll need it
later in the course anyway). Make sure to find a good code to do this, with
pivoting, not just a straight Gauss-Jordan elimination code, or, heaven
forfend, Cramer's rule. Please submit your code, noting where you got it from.
"""
# Using numpy matrix module
import numpy as np
import numpy.matlib
# 5x5 random matrix
M = numpy.matlib.rand(5,5)
# The inverse
N = M.I
print(M)
print(N)
# Gives the identity matrix
print(M.dot(N))
