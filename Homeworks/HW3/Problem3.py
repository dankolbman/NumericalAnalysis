import numpy as np
import matplotlib.pyplot as plt
import math
import random

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
font = {'family' : 'normal','size'   : 16}
rc('font', **font)

# Simpson's method integration
def simpson(x, y):
  h = ( x[-1] - x[0] )/len(x)
  tot = y[0] + y[-1]
  # Odd Terms
  for i in range(1, len(x), 2):
    tot += 4*y[i]
  # Even Terms
  for i in range(2, len(x)-1, 2):
    tot += 2*y[i]
  return tot*h/3

# Trapezoid integration
def trapezoid(x, y):
  h = ( x[-1] - x[0] )/len(x)
  tot = y[0]/2 + y[-1]/2
  for i in range(1,len(x)):
    tot += y[i]
  return tot*h

# Spline interpolation  
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

# Luminosity from magnitude
def lum(m):
  return 8.85*10**(-0.4*m)
################################################################################

t = np.arange(0.0, 1.01, 0.1)
print(t)
M = [0.302, 0.264, 0.185, 0.106, 0.093, 0.24, 0.579, 0.561, 0.468, 0.387, 0.302]
# Luminosity from magnitude
L = [ lum(i) for i in M ]

# Integrate it
print('Integrals from data only')
print('Area from Simpson\'s method', simpson(t, L) )
print('Area from trapezoid rule', trapezoid(t, L) )

# Interpolate it 
# Use magnitudes
n = len(t)
x = []
fx = []
sol = spline(t, M)
pts = 500
for i in range(0,n-1):
  dx = t[i+1]-t[i]
  for j in range(pts):
    bb = 1*j/(pts)
    aa = 1 - bb
    x.append(t[i]+bb*dx)
    cc = dx**2*aa*(aa**2-1)/6
    dd = dx**2*bb*(bb**2-1)/6
    fx.append(aa*M[i]+bb*M[i+1]+cc*sol[i]+dd*sol[i+1])
print('Interpolating and integrating on magnitude')
print('Energy from Simpson\'s method', lum(simpson(x, fx)))
print('Energy from trapezoid rule', lum(simpson(x, fx)))

# Use luminosities 
n = len(t)
x = []
fx = []
sol = spline(t, L)
pts = 500
for i in range(0,n-1):
  dx = t[i+1]-t[i]
  for j in range(pts):
    bb = 1*j/(pts)
    aa = 1 - bb
    x.append(t[i]+bb*dx)
    cc = dx**2*aa*(aa**2-1)/6
    dd = dx**2*bb*(bb**2-1)/6
    fx.append(aa*L[i]+bb*L[i+1]+cc*sol[i]+dd*sol[i+1])
print('Interpolating and integrating on luminosity')
print('Energy from Simpson\'s method', simpson(x, fx))
print('Energy from trapezoid rule', simpson(x, fx))

plt.plot(x, fx)
plt.plot(t, L, 'ro', markersize=12)
plt.title('Luminosity with Cubic Spline Interpolation')
plt.savefig('Problem3.png')
plt.show()
