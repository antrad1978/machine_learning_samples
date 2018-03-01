from sklearn import *
import sklearn
bs = sklearn.cross_validation.Bootstrap(9, random_state=0)
len(bs)
print(bs)
for train_index, test_index in bs:
    print("TRAIN:", train_index, "TEST:", test_index)