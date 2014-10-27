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
  return 1/(1+(t)**2)

def chebyshev(n, func):
  pts = []
  coeff = np.zeros(n)
  for k in range(n):
    pts.append(math.cos(math.pi*(2*k-1)/(2*n)))
  
  for i in range(n):
    for j in range(n):
      coeff[i] += func( pts[j]*5 ) * math.cos( i*math.acos( pts[j] ))
    coeff[i] /= n/2
  coeff[0] /= 2
  return coeff


#######

# The function
x = [ i/100 for i in range(-500,500) ]
fx = [ f(i) for i in x ]
plt.plot(x,fx, 'k',label='f(t)', linewidth=5, alpha=0.5)

### 5 points
x, y = [], []
n = 5
co = chebyshev(n ,f)
for i in range(1000):
  x.append( 2*i/1000-1 )
  yv = 0
  for j in range(n):
    yv += co[j] * math.cos( j*(math.acos( x[-1] ) ))
  y.append(yv)

x = [ i*5 for i in x ]
plt.plot(x, y, label='5 Points')

diffs = [ f( x[i] ) - y[i] for i in range(len(x)) ]
rmse=np.linalg.norm( diffs )/np.sqrt(len(fx))
print('Error for 5 Points:', rmse)


### 10 points
x, y = [], []
n = 10
co = chebyshev(n ,f)
for i in range(1000):
  x.append( 2*i/1000-1 )
  yv = 0
  for j in range(n):
    yv += co[j] * math.cos( j*(math.acos( x[-1] ) ))
  y.append(yv)

x = [ i*5 for i in x ]
plt.plot(x, y, label='10 Points')


diffs = [ f( x[i] ) - y[i] for i in range(len(x)) ]
rmse=np.linalg.norm( diffs )/np.sqrt(len(fx))
print('Error for 10 Points:', rmse)

### 15 points
x, y = [], []
n = 15
co = chebyshev(n ,f)
for i in range(1000):
  x.append( 2*i/1000-1 )
  yv = 0
  for j in range(n):
    yv += co[j] * math.cos( j*(math.acos( x[-1] ) ))
  y.append(yv)

x = [ i*5 for i in x ]
plt.plot(x, y, label='15 Points')

diffs = [ f( x[i] ) - y[i] for i in range(len(x)) ]
rmse=np.linalg.norm( diffs )/np.sqrt(len(fx))
print('Error for 15 Points:', rmse)

plt.legend(fontsize=16)
plt.title('Chebyshev Polynomial for $f(t)$')
plt.savefig('Problem5iii.png')
plt.show()
