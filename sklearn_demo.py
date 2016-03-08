#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import numpy as np
import pylab as pl
from sklearn import datasets,svm,random_projection,neighbors,cluster
from sklearn.externals import joblib

# 线性核
# svc = svm.SVC(kernel=’linear’)
# 多项式核
# svc = svm.SVC(kernel=’poly’, … degree=3) # degree: polynomial degree
# RBF核(径向基函数)5
# svc = svm.SVC(kernel=’rbf’) # gamma: inverse of size of # radial kernel



import pickle
reload(sys)
sys.setdefaultencoding('utf-8')
iris = datasets.load_iris()
x,y = iris.data,iris.target
digits = datasets.load_digits()

print(digits.data)
print np.unique(iris.target)
#pl.imshow(digits.images[0],cmap=pl.cm.gray_r)
#pl.show()

clf = svm.SVC(gamma=0.001,C=100.)
print clf.fit(iris.data,iris.target)
print clf.fit(digits.data[:-1],digits.target[:-1])
print clf.fit(x,y)
print clf.predict([[ 5.0,  3.6,  1.3,  0.25]])


#K最近邻(KNN)分类器
knn = neighbors.KNeighborsClassifier()
print knn.fit(x,y)
print knn.predict([[0.1,0.2,0.3,0.4]])

#k-means聚类
k_means = cluster.KMeans(n_clusters=3)
print k_means.fit(iris.data)
print k_means.labels_[::10]
print iris.target[::10]


s = pickle.dumps(clf)
clf2 = pickle.loads(s)

print clf2.predict(x[0:1])
print joblib.dump(clf,'filename.pkl')
print joblib.load('filename.pkl')

rng = np.random.RandomState(0)
X = rng.rand(10,2000)
X = np.array(X,dtype='float32')
transformer = random_projection.GaussianRandomProjection()
x_new = transformer.fit_transform(X)
print x_new.dtype

print X.dtype
print X














def run():
    print "hello"


if __name__ == "__main__":
    run()    