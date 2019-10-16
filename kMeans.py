import numpy as np
import matplotlib.pyplot as plt
import random

# Define Parameters
N = 300
K = 3
epochs = 20

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

for e in range(epochs):
	segmentedPoints = [np.empty((0,2)) for i in range(K)]
	for j in range(N):
		centroidDist = (points[j]-c)**2
		centroidDist = centroidDist.sum(axis=1)
		segmentedPoints[np.argmin(centroidDist)] = np.append(segmentedPoints[np.argmin(centroidDist)],points[j].reshape(1,2), axis=0)
	# Recompute centroids
	for k in range(K):
		c[k] = segmentedPoints[k].mean(axis=0)

	# plot points
	colors = "bgcmykw"
	#plt.clear()
	print("segmentedPoints: ", segmentedPoints[0].mean(), segmentedPoints[1].mean(), segmentedPoints[2].mean())
	for p in range(K):
		plt.scatter(segmentedPoints[p][:,0],segmentedPoints[p][:,1],c=colors[p])
	# plt.scatter(segmentedPoints[1][:,0],segmentedPoints[1][:,1],c='y')
	# plt.scatter(segmentedPoints[2][:,0],segmentedPoints[2][:,1],c='g')
	removable = plt.scatter(c[:,0], c[:,1], c='r', marker='^')
	plt.show(block=False)
	plt.pause(0.2)
	plt.savefig('plots/plot_'+str(e)+'.png')
	removable.remove()

print("segmentedPoints: ", segmentedPoints[0][:,0], len(segmentedPoints[1]), len(segmentedPoints[2]))

