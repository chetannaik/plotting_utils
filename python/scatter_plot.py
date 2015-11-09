import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


M=np.loadtxt(open("for_heatmap.txt"))
print M
# N = 50
x = M.shape[0]
y = M.shape[1]

tups=[]
for i in range(x):
    for j in range(y):
      tups+=[(i,j,M[i][j])]

[x,y,z]=zip(*tups)

# colors = np.random.rand(N)
# area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses
cm = plt.cm.get_cmap('RdYlBu')
# g=plt.scatter(x, y, s=area, c=colors, alpha=0.5)
g=plt.scatter(x, y, s=50, c=z, alpha=0.5,marker='s',cmap=cm)
# g=plt.scatter(x, y, s=50, c=z, alpha=0.5,marker='s',cmap=cm,vmin=0, vmax=20)

# ax = g
# ax.add_patch(Rectangle((3, 4), 1, 1, fill=False, edgecolor='blue', lw=3))

# plt.gray()
plt.show()
