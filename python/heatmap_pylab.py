import pylab as pl
import matplotlib
data = pl.random((1,25)) # 25x25 matrix of values
print data,type(data)
pl.pcolor(data)
pl.pcolor(data, cmap=matplotlib.cm.Blues)
pl.colorbar()
pl.show()
