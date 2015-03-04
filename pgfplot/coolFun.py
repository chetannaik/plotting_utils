# coding: utf-8
import numpy  as np
X = np.linspace(-0.75,-0.1,50,endpoint=True)
for a in range(1,5):
    coolFun= abs(np.exp(-X)/(1+X)**a)
    # print coolFun 
    print a
    for x,cool in zip(X,coolFun):
        print x,cool
    print
