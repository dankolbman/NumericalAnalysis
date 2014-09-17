# Using numpy matrix module
import numpy as np
import numpy.matlib
# 5x5 random matrix
M = numpy.matlib.rand(3,3)
# The inverse
N = M.I
print("A matrix:")
print(M)
print("The inverse of that matrix:")
print(N)
# Gives the identity matrix
print("The two multiplied together (should be the identity matrix):")
print(M.dot(N))
