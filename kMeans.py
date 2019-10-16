import numpy as np
import matplotlib.pyplot as plt
import random

# Define Parameters
N = 500
K = 10
epochs = 30

# Generate n random points
points = np.random.random_sample((N,2))
#points = np.tanh(points)


# K Means
# select a random point
c1Indices = np.random.randint(N,size=1)
c = points[c1Indices]

for i in range(1, K):
	dist = np.zeros((N,))
	for j in range(i):
		tempSquares = (points - c[len(c)-j-1])**2
		dist += tempSquares.sum(axis=1)
	tempIndices = np.argmax(dist)
	c=np.append(c,points[tempIndices].reshape((1,2)), axis=0)
print("Centroid Initialization Complete")

# generate colors
colors = np.random.rand(3,K)

for e in range(epochs):
	segmentedPoints = [np.empty((0,2)) for i in range(K)]
	for j in range(N):
		centroidDist = (points[j]-c)**2
		centroidDist = centroidDist.sum(axis=1)
		segmentedPoints[np.argmin(centroidDist)] = np.append(segmentedPoints[np.argmin(centroidDist)],points[j].reshape(1,2), axis=0)
	# Recompute centroids
	for k in range(K):
		if len(segmentedPoints[k])>0:
			c[k] = segmentedPoints[k].mean(axis=0)

	# plot points
	for p in range(K):
		plt.scatter(segmentedPoints[p][:,0],segmentedPoints[p][:,1],c=colors[:,p], marker='o')
	# plt.scatter(segmentedPoints[1][:,0],segmentedPoints[1][:,1],c='y')
	# plt.scatter(segmentedPoints[2][:,0],segmentedPoints[2][:,1],c='g')
	removable = plt.scatter(c[:,0], c[:,1], c='r', marker='^')
	plt.show(block=False)
	plt.pause(0.1)
	plt.savefig('plots/plot_'+str(e)+'.png')
	removable.remove()
print("Done")