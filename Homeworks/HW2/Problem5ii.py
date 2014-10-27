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

### The function
def f(t):
  return 1/(1+t**2)

# Spline
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


#######

# The function
x = [ i/100 for i in range(-500,500) ]
fx = [ f(i) for i in x ]
plt.plot(x,fx, 'k--',label='f(t)', linewidth=5)

### 5 points
xpts = np.linspace(-5, 5, 5)
ypts = [ f(t) for t in xpts ]
sol = spline(xpts, ypts)
n = len(xpts)
x = []
fx = []
t = 1000
for i in range(0,n-1):
  dx = xpts[i+1]-xpts[i]
  for j in range(t):
    bb = 1*j/(t)
    aa = 1 - bb
    x.append(xpts[i]+bb*dx)
    cc = dx**2*aa*(aa**2-1)/6
    dd = dx**2*bb*(bb**2-1)/6
    fx.append(aa*ypts[i]+bb*ypts[i+1]+cc*sol[i]+dd*sol[i+1])

plt.plot(x,fx, 'r', label='5 Points')

diffs = [ f( x[i] ) - fx[i] for i in range(len(x)) ]
rmse=np.linalg.norm( diffs )/np.sqrt(len(fx))
print('Error for 5 Points:', rmse)

### 10 points
xpts = np.linspace(-5, 5, 10)
ypts = [ f(t) for t in xpts ]
sol = spline(xpts, ypts)
n = len(xpts)
x = []
fx = []
t = 1000
for i in range(0,n-1):
  dx = xpts[i+1]-xpts[i]
  for j in range(t):
    bb = 1*j/(t)
    aa = 1 - bb
    x.append(xpts[i]+bb*dx)
    cc = dx**2*aa*(aa**2-1)/6
    dd = dx**2*bb*(bb**2-1)/6
    fx.append(aa*ypts[i]+bb*ypts[i+1]+cc*sol[i]+dd*sol[i+1])

plt.plot(x,fx, 'b', label='10 Points')

diffs = [ f( x[i] ) - fx[i] for i in range(len(x)) ]
rmse=np.linalg.norm( diffs )/np.sqrt(len(fx))
print('Error for 10 Points:', rmse)

### 15 points
xpts = np.linspace(-5, 5, 15)
ypts = [ f(t) for t in xpts ]
sol = spline(xpts, ypts)
n = len(xpts)
x = []
fx = []
t = 1000
for i in range(0,n-1):
  dx = xpts[i+1]-xpts[i]
  for j in range(t):
    bb = 1*j/(t)
    aa = 1 - bb
    x.append(xpts[i]+bb*dx)
    cc = dx**2*aa*(aa**2-1)/6
    dd = dx**2*bb*(bb**2-1)/6
    fx.append(aa*ypts[i]+bb*ypts[i+1]+cc*sol[i]+dd*sol[i+1])

plt.plot(x,fx, 'g', label='15 Points',linewidth=3)

diffs = [ f( x[i] ) - fx[i] for i in range(len(x)) ]
rmse=np.linalg.norm( diffs )/np.sqrt(len(fx))
print('Error for 15 Points:', rmse)

plt.legend(fontsize=16)
plt.ylim( [-0.2, 1.1] )
plt.title('Natural Cubic Splines for $f(t)$')
plt.savefig('Problem5ii.png')
plt.show()
