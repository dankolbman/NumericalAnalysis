import math
import copy
import matplotlib.pyplot as plt

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
font = {'family' : 'normal',
        'size'   : 24}

rc('font', **font)

def interp(t, xpts, ypts):
  x = copy.deepcopy(xpts)
  y = copy.deepcopy(ypts)

  # Iterate through the first N-1 points
  for i in range(1,len(xpts)):
    for j in range(0,len(xpts)-1):
      x[j] = (1-t)*x[j] + t*x[j+1]
      y[j] = (1-t)*y[j] + t*y[j+1]

  return x[0], y[0]

xt = [ (1+6*(t/100)**2+2*(t/100)**3) for t in range(0, 100) ]
yt = [ (1-(t/100)+(t/100)**3) for t in range(0, 100) ]

xpts = [ 1, 1, 3, 9 ]
ypts = [ 1, 2/3, 1/3, 1 ]

x = []
y = []


for t in range(0,1000):
  x1, y1 = interp(t/1000, xpts, ypts)
  x.append(x1)
  y.append(y1)

plt.plot(xt, yt, 'r', label='Parmetric Curve', linewidth=10, alpha=0.5)
plt.plot(x,  y,  'b', label='Bezier Curve', linewidth=3, alpha=1.0)
plt.plot(xpts, ypts, 'ko-', label='Control Points', markersize=10)
plt.xlim( [-1, 10] )
plt.ylim( [0.2, 1.2] )
plt.legend(loc=9, fontsize=16)
plt.savefig('Problem3.png')
plt.show()
