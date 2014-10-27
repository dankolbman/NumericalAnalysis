import math
import scipy.interpolate as intrp
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
font = {'family' : 'normal',
        'size'   : 24}

rc('font', **font)

t = [ 0.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0 ]
mag = [ 0.302, 0.185, 0.106, 0.093, 0.24, 0.579, 0.561, 0.468, 0.302 ]

def spline(xpts, ypts):
  n = len(xpts)
  mat = np.zeros(( n, n))
  rhs = np.zeros(( n,1 ))
  for i in range(1,n-1):
    rhs[i] = 6 * ( (ypts[i+1]-ypts[i]) / (xpts[i+1]-xpts[i]) \
            -(ypts[i]-ypts[i-1]) / (xpts[i]-xpts[i-1]) )
    
    for j in range(0,n-1):
      # Set triagonal elements
      if(j==i-1): mat[i][j] += xpts[i] - xpts[i-1]
      elif(j==i): mat[i][j] += 2*(xpts[i+1]-xpts[i-1])
      elif(j==i+1): mat[i][j] += xpts[i+1]-xpts[i]

  # BCs
  mat[0][0] = 1
  mat[-1][-1] = 1
  rhs[0] = 0
  rhs[-1] = 0
  # Solve it
  x_vec = np.linalg.solve(mat, rhs)
  return x_vec

fit = intrp.lagrange(t, mag)

x = [ i/1000 for i in range(1000) ]
y = [ fit(i) for i in x ]

plt.plot(t, mag, 'ro', markersize = 10, label='Original Data')
plt.plot(x, y, label='Lagrange Interpolating Polynomial')

# Spline fit
n = len(t)
x = []
fx = []
sol = spline(t, mag)
pts = 1000
for i in range(0,n-1):
  dx = t[i+1]-t[i]
  for j in range(pts):
    bb = 1*j/(pts)
    aa = 1 - bb
    x.append(t[i]+bb*dx)
    cc = dx**2*aa*(aa**2-1)/6
    dd = dx**2*bb*(bb**2-1)/6
    fx.append(aa*mag[i]+bb*mag[i+1]+cc*sol[i]+dd*sol[i+1])

plt.plot(x, fx, label='Natural Spline')
plt.xlim([-0.1, 1.1])
plt.title('Cepheid Magnitude')
plt.xlabel('Time')
plt.ylabel('Apparent Magnitude')
plt.legend(loc=0, fontsize=16)
plt.tight_layout()
plt.savefig('Problem8.png')
plt.show()
