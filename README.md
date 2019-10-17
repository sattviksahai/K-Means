# K-Means
A numpy implementation of K-Means Clustering using Lloyd's Algorithm

**Initialization**
Choose K centroids for K clusters
1. Choose any random data point as the first centroid (C<sub>1</sub>)
2. Choose subsequent centroids as per the following formula:
$$c_k = max(\sum_{i=1}^{k} \left|\left|x_j-c_i\right|\right|_2^2)$$

**Allocate points to centroids**
Allocate every point x<sub>j</sub> to a cluster as per the following formula
$$min(\left|\left|x_j-c_i\right|\right|_2^2)\qquad for\,i\in\[k\]$$

**Re-compute centroids**
Re-Compute centroids for all clusters as per the following formula
$$ \hat c_i = \frac {1} {|S_i|} \sum_{j \in S_i}x_j\qquad for\,all\,clusters\,S_i $$


***The allocation and re-computation steps are repeated until the clusters stablize***


**Clustering in action**
<center>![](10ClassAnimation.gif)
<i>10 clusters</i>
![](3ClassAnimation.gif)
<i>3 clusters</i>
</center>