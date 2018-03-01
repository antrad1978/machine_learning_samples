from sklearn import datasets

data=datasets.load_iris()
print("Features: %s" % data.feature_names)
features=data.data
#labels=data.target

#print(data.target)

from sklearn.cluster import MiniBatchKMeans, KMeans

k_means = KMeans(n_clusters=3, init='k-means++',max_iter=999,n_init=1,random_state=101)

k_means.fit(features)

print(k_means.cluster_centers_)
