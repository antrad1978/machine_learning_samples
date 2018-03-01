# X as training data and y as target values
X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]
from sklearn.neighbors import KNeighborsClassifier
#use distance as metric, check here documentation about:
#http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
neigh = KNeighborsClassifier(n_neighbors=3, weights="distance")
neigh.fit(X, y)
print(neigh.predict([[1.1]]))
