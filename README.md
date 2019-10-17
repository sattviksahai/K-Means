# K-Means
A numpy implementation of K-Means Clustering using Lloyd's Algorithm

**Initialization**
Choose K centroids for K clusters
1. Choose any random data point as the first centroid (C<sub>1</sub>)
2. Choose subsequent centroids as per the following formula:
![](equation1.png)

**Allocate points to centroids**
Allocate every point x<sub>j</sub> to a cluster as per the following formula
![](equation2.png)

**Re-compute centroids**
Re-Compute centroids for all clusters as per the following formula
![](equation3.png)

***The allocation and re-computation steps are repeated until the clusters stablize***


**Clustering in action**

![](10ClassAnimation.gif)
<i>10 clusters</i>
![](3ClassAnimation.gif)
<i>3 clusters</i>