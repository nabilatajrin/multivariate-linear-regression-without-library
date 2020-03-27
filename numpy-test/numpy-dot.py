import numpy.matlib
import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])

x = np.dot(a,b)

print(x)


# This 'np.dot(X, w)' function returns the dot product of two arrays. For 2-D vectors, it is the equivalent to matrix
# multiplication. For 1-D arrays, it is the inner product of the vectors. For N-dimensional arrays, it is a sum product
# over the last axis of a and the second-last axis of b.