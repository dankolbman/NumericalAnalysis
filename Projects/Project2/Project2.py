import matplotlib.pyplot as plt
import numpy as np
import math

# The given function
def func(x):
  return -math.cos(x-0.2)
  #return 1-x**2
  #return math.sqrt(5-x**2)

def func_deriv(x):
  return -math.sin(0.2-x)
  #return -2*x
  #return -x/(math.sqrt(5-x**2))

### Spline stuff
# Takes x, y coords and  y1', yn' BCs
def spline(xpts, ypts, y1, yn):
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

  # Clamped BCs
  mat[0][0] = 2
  mat[0][1] = 1
  mat[-1][-1] = 2
  mat[-2][-1] = 1
  rhs[0] = 6*((ypts[1] - ypts[0]) / (xpts[1]-xpts[0]) - y1)
  rhs[-1] = 6*(yn - (ypts[n-1]-ypts[n-2]) / (xpts[n-1]-xpts[n-2]))
  return np.linalg.solve(mat, rhs)

# Get data stuff
x, y, dxdy = [], [], []
fname = 'input.dat'
fname = input('Enter point file name (default: input.dat): ')
if fname == '':
  fname = 'input.dat'
try:
  f = open(fname)
except IOError:
  print('Had trouble opening the specified file!!')
  exit()

# Read point values
for line in f:
  l = line.split()
  try:
    x.append(float(l[0]))
    y.append(float(l[1]))
    dxdy.append(float(l[2]))
  except (IndexError, ValueError):
    print('Input file was not formatted correctly')

f.close()

# Get the spline thing
# Use derivatives at ends for clamped bcs
sol0 = spline(x, y, dxdy[0], dxdy[-1])
# Change the value of the derivative of the last knot
sol1 = spline(x, y, dxdy[0], dxdy[-1]*2)

# Plot things
x_spline0, y_spline0 = [], []
x_spline1, y_spline1 = [], []
n = len(x)
t = 200             # Number of sample points
for i in range(0,n-1):
  dx = x[i+1]-x[i]
  for j in range(t):
    bb = j/(t)
    aa = 1 - bb
    x_spline0.append(x[i]+bb*dx)
    x_spline1.append(x[i]+bb*dx)
    cc = dx**2*aa*(aa**2-1)/6
    dd = dx**2*bb*(bb**2-1)/6
    y_spline0.append(aa*y[i]+bb*y[i+1]+cc*sol0[i]+dd*sol0[i+1])
    y_spline1.append(aa*y[i]+bb*y[i+1]+cc*sol1[i]+dd*sol1[i+1])

x_exact = [ i/100 for i in range(-100,100) ]
y_exact = [ func(i) for i in x_exact ]
# Plot original data
plt.plot(x, y, 'ro', markersize=10, label='Given Data')
# Plot the exact function
plt.plot(x_exact, y_exact, 'k--',label='Exact Function', linewidth=5, alpha=0.5)
# Plot spline
plt.plot(x_spline0, y_spline0, 'r', label='Clamped Spline', linewidth=3, alpha=0.5)
# Plot spline
plt.plot(x_spline1, y_spline1, 'b',label='With $2y_5^\prime$', linewidth=3, alpha=0.5)
plt.legend(fontsize=16, loc=0)
plt.title('Reflector Surface', fontsize=28)
plt.savefig('output.png')

### Error analysis
# Get differences from the exact values we have data for on the spline
# NB we can do this because the interpolation points are spaced evenly.
# If they weren't, there would be different point densities for different
# interpolation segments and the rmse wouldn't be evenly weighted
diffs0 = [ y_spline0[i]-func(x_spline0[i]) for i in range(len(x_spline0)) ]
diffs1 = [ y_spline1[i]-func(x_spline1[i]) for i in range(len(x_spline1)) ]
rmse0 = np.linalg.norm(diffs0)/np.sqrt(len(diffs0))
rmse1 = np.linalg.norm(diffs1)/np.sqrt(len(diffs1))
print('RMSE for spline fit:',rmse0)
print('RMSE for spline with 2*y_5`:',rmse1)
print('Saved image to output.png')
plt.show()

### Derivatives
y_exact_deriv = [ func_deriv(i) for i in x_exact ]
# Central derivative
spline_deriv = [ (y_spline0[i+1]-y_spline0[i-1]) / (x_spline0[i+1]-x_spline0[i-1])\
     for i in range(1,len(x_spline0)-1) ]

# The know derivative
plt.plot(x_exact, y_exact_deriv, 'k--', label='Analytic Derivative', linewidth=5, alpha=0.5)
# The spline derivative
plt.plot(x_spline0[1:-1], spline_deriv, 'r', label='Spline Derivative', linewidth=3, alpha=0.5)
plt.legend(fontsize=16, loc=0)
plt.title('Surface Derivative',fontsize=28)
plt.savefig('deriv.png')
print('Saved derivative image to deriv.png')
plt.show()

diffs = [ spline_deriv[i-1]-func_deriv(x_spline0[i]) for i in range(1,len(x_spline0)-1) ]
rmse = np.linalg.norm(diffs)/np.sqrt(len(diffs))
print('RMSE for derivative:',rmse)
