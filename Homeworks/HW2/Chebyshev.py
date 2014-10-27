import math
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
font = {'family' : 'normal',
        'size'   : 24}
rc('font', **font)

import copy

def f(x):
  return 1/(1+x**2)

def interp(n, func):
  pts = []
  coeff = np.zeros(n)
  for k in range(n):
    pts.append(math.cos(math.pi*(2*k-1)/(2*n)))
  
  for i in range(n):
    for j in range(n):
      coeff[i] += func( pts[j] ) * math.cos( i*math.acos( pts[j] ))
    coeff[i] /= n/2
  coeff[0] /= 2
  return coeff


x, y = [], []
n = 20
co = interp(n ,f)
for i in range(1000):
  x.append( 2*i/1000-1 )
  yv = 0
  for j in range(n):
    yv += co[j] * math.cos( j*(math.acos( x[-1] ) ))
  y.append(yv)

plt.plot(x,y)
plt.show()
