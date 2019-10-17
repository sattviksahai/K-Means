# K-Means
A numpy implementation of K-Means Clustering using Lloyd's Algorithm

**Initialization**
Choose K centroids for K clusters
1. Choose any random data point as the first centroid (C<sub>1</sub>)
2. Choose subsequent centroids as per the following formula:
<center>![](equation1.png)</center>

**Allocate points to centroids**
Allocate every point x<sub>j</sub> to a cluster as per the following formula
<center>![](equation2.png)</center>

**Re-compute centroids**
Re-Compute centroids for all clusters as per the following formula
<center>![](equation3.png)</center>

***The allocation and re-computation steps are repeated until the clusters stablize***


**Clustering in action**
<center>![](10ClassAnimation.gif)
<i>10 clusters</i>
![](3ClassAnimation.gif)
<i>3 clusters</i>
</center>