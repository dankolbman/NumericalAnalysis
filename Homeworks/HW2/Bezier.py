import math
import matplotlib.pyplot as plt

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
font = {'family' : 'normal',
        'size'   : 24}
rc('font', **font)

import copy

def interp(t, xpts, ypts):
  x = copy.deepcopy(xpts)
  y = copy.deepcopy(ypts)

  # Iterate through the first N-1 points
  for i in range(1,len(xpts)):
    for j in range(0,len(xpts)-1):
      x[j] = (1-t)*x[j] + t*x[j+1]
      y[j] = (1-t)*y[j] + t*y[j+1]

  return x[0], y[0]

xpts = [ 1, 1, 3, 9 ]
ypts = [ 1, 2/3, 1/3, 1 ]

x = []
y = []


for t in range(0,1000):
  x1, y1 = interp(t/1000, xpts, ypts)
  x.append(x1)
  y.append(y1)

plt.plot(x,y)
plt.show()

