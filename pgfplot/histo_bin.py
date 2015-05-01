# coding: utf-8
import numpy as np
X=np.loadtxt('news.data')
numbins=4
bins=np.arange(X.min(),X.max(),(X.max()-X.min())/numbins)
inds = np.digitize(X, bins)
binSizes=[(inds==i).sum() for i in range(1,numbins+1)]
print sum(binSizes)
