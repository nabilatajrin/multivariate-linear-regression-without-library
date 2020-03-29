import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pylab as plt

# load the data
X = []
Y = []
for line in open('data-2d.csv'):
    x1, x2, y = line.split(',')
    X.append([float(x1), float(x2), 1])
    Y.append(float(y))

# let's turn X and Y into numpy arrays since that will be useful later
X = np.array(X)
Y = np.array(Y)


# let's plot the data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], Y)
plt.show()


w = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Y))
Yhat = np.dot(X, w)


# Calculate the mean value of a list of numbers
#or np.mean(Y)
def mean(values):
    return sum(values) / float(len(values))

print('y mean: ', mean(Y))

ssr = np.sum((Yhat - mean(Y))**2)
sse = np.sum((Y - Yhat)**2)
sst = np.sum((Y - mean(Y))**2)

sst2 = ssr + sse


print("\nthe sum of square(model/regression) is:", ssr)
print("\nthe sum of square(residual/error) is:", sse)
print("the the sum of square(total) is:", sst)
print("sst2: ", sst2)


# determine how good the model is by computing the r-squared
r2 = 1 - ssr / sst
print("\nthe r-squared is:", r2)