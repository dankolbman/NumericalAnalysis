import numpy as np
import math
import matplotlib.pyplot as plt

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
font = {'family' : 'normal',
        'size'   : 24}
rc('font', **font)




xpts = [ 0, 1, 2, 3 ]
ypts = [ 3, 5, 4, 1 ]
# BC specific parameters
c1 = 5
cn = -5

x = []
y = []

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

# Apply BCs
# Natural
def natural(mat, rhs):
  mat[0][0] = 1
  mat[-1][-1] = 1
  rhs[0] = 0
  rhs[-1] = 0

# Curvature
def curvature(mat, rhs):
  c1 = float(input('y_1``: '))
  cn = float(input('y_n``: '))
  mat[0][0] = 1
  mat[-1][-1] = 1
  rhs[0] = c1
  rhs[-1] = cn
  print(rhs)

# Clamped
def clamped(mat, rhs):
  c1 = float(input('y_1`: '))
  cn = float(input('y_n`: '))
  mat[0][0] = 2
  mat[0][1] = 1
  mat[-1][-1] = 2
  mat[-1][-2] = 1
  rhs[0] = 6*((ypts[1] - ypts[0]) / (xpts[1]-xpts[0]))
  rhs[-1] = 6*(cn - (ypts[n-1]-ypts[n-2]) / (xpts[n-1]-xpts[n-2]))

# Parabolic
def parabolic(mat, rhs):
  mat[0][0] = 1
  mat[0][1] = -1
  mat[-1][-1] = 1
  mat[-1][-2] = -1
  rhs[0] = 0
  rhs[-1] = 0

# Not a knot
def notKnot(mat, rhs):
  mat[0][0] = xpts[2]-xpts[1]
  mat[0][1] = xpts[0]-xpts[2]
  mat[0][2] = xpts[1]-xpts[0]
  mat[-1][-1] = xpts[n-2]-xpts[n-3]
  mat[-1][-2] = xpts[n-3]-xpts[n-1]
  mat[-1][-3] = xpts[n-1]-xpts[n-2]
  rhs[0] = 0
  rhs[-1] = 0

# BC dict to map input to functions
bcs = { 1:natural, 2:curvature, 3:clamped, 4:parabolic, 5:notKnot }

method = input("Enter type of boundary condition (1: natural, 2: curvature,\
 3: clamped, 4: parabolic, 5: not a knot):\n")

try:
  bcs[int(method)](mat, rhs)
except KeyError:
  print("Not a valid method")
  exit()

# Solve ax=b
x_vec = np.linalg.solve(mat, rhs)
print('a matrix:')
print(mat)
print('b matrix:')
print(rhs)
print('Solution vector:')
print(x_vec)
t = 1000
for i in range(0,n-1):
  dx = xpts[i+1]-xpts[i]
  for j in range(t):
    bb = 1*j/(t)
    aa = 1 - bb
    x.append(xpts[i]+bb*dx)
    cc = dx**2*aa*(aa**2-1)/6
    dd = dx**2*bb*(bb**2-1)/6
    y.append(aa*ypts[i]+bb*ypts[i+1]+cc*x_vec[i]+dd*x_vec[i+1])

plt.plot(x, y)
plt.show()
#exit()

#### SUPER HACK
x, y = [], []
bcs[1](mat, rhs)
x_vec = np.linalg.solve(mat, rhs)
t = 1000
for i in range(0,n-1):
  dx = xpts[i+1]-xpts[i]
  for j in range(t):
    bb = 1*j/(t)
    aa = 1 - bb
    x.append(xpts[i]+bb*dx)
    cc = dx**2*aa*(aa**2-1)/6
    dd = dx**2*bb*(bb**2-1)/6
    y.append(aa*ypts[i]+bb*ypts[i+1]+cc*x_vec[i]+dd*x_vec[i+1])
plt.plot(x, y, label='Natural') 

x, y = [], []
bcs[2](mat, rhs)
x_vec = np.linalg.solve(mat, rhs)
t = 1000
for i in range(0,n-1):
  dx = xpts[i+1]-xpts[i]
  for j in range(t):
    bb = 1*j/(t)
    aa = 1 - bb
    x.append(xpts[i]+bb*dx)
    cc = dx**2*aa*(aa**2-1)/6
    dd = dx**2*bb*(bb**2-1)/6
    y.append(aa*ypts[i]+bb*ypts[i+1]+cc*x_vec[i]+dd*x_vec[i+1])
plt.plot(x, y, label='Curvature')

x, y = [], []
bcs[3](mat, rhs)
x_vec = np.linalg.solve(mat, rhs)
t = 1000
for i in range(0,n-1):
  dx = xpts[i+1]-xpts[i]
  for j in range(t):
    bb = 1*j/(t)
    aa = 1 - bb
    x.append(xpts[i]+bb*dx)
    cc = dx**2*aa*(aa**2-1)/6
    dd = dx**2*bb*(bb**2-1)/6
    y.append(aa*ypts[i]+bb*ypts[i+1]+cc*x_vec[i]+dd*x_vec[i+1])
plt.plot(x, y, label='Clamped')


x, y = [], []
bcs[4](mat, rhs)
x_vec = np.linalg.solve(mat, rhs)
t = 1000
for i in range(0,n-1):
  dx = xpts[i+1]-xpts[i]
  for j in range(t):
    bb = 1*j/(t)
    aa = 1 - bb
    x.append(xpts[i]+bb*dx)
    cc = dx**2*aa*(aa**2-1)/6
    dd = dx**2*bb*(bb**2-1)/6
    y.append(aa*ypts[i]+bb*ypts[i+1]+cc*x_vec[i]+dd*x_vec[i+1])
plt.plot(x, y, label='Parabolic')

x, y = [], []
bcs[5](mat, rhs)
x_vec = np.linalg.solve(mat, rhs)
t = 1000
for i in range(0,n-1):
  dx = xpts[i+1]-xpts[i]
  for j in range(t):
    bb = 1*j/(t)
    aa = 1 - bb
    x.append(xpts[i]+bb*dx)
    cc = dx**2*aa*(aa**2-1)/6
    dd = dx**2*bb*(bb**2-1)/6
    y.append(aa*ypts[i]+bb*ypts[i+1]+cc*x_vec[i]+dd*x_vec[i+1])
plt.plot(x, y, label='Not a Knot')

plt.legend(loc=3, fontsize=16)
plt.title('Cubic Spline Interpolation')
plt.savefig('spline.png')
plt.show()

