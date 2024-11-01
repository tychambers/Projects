# Unsupervised: find K amount of clusters
# then you can assign a value to the cluster
# K number of centroids and points

from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits

digits = load_digits()
data = scale(digits.data)

model = KMeans(n_clusters=10, init='random', n_init=10)
model.fit(data)

# Make prediction below
# model.predict([])
