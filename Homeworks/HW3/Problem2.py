import numpy as np
import matplotlib.pyplot as plt
import math
import random

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
font = {'family' : 'normal','size'   : 12}
rc('font', **font)

def f(x):
  return math.sin(x)*math.exp(math.cos(x))

# The integral of f(x)
def F(x):
  return -math.exp(math.cos(x))

# The derivative of f(x)
def f_prime(x):
  return ( math.cos(x) - math.sin(x)**2 )*math.exp( math.cos(x) )

# The second derivative of f(x)
def f_prime2(x):
  return (math.sin(x)**2-3*math.cos(x)-1)*math.exp(math.cos(x))*math.sin(x)

def g(x):
  return f(x) + (random.random()-0.5) * 2e-3

def stencil(x, fx):
  d = []
  for i in range( 2, len(x)-2 ):
    di = -fx[ i+2 ] + 8*fx[ i+1 ] - 8*fx[i-1] + fx[ i-2 ]
    di /= 12*( x[1]-x[0] )
    d.append(di)
  return d

def stencil2(x, fx):
  d = []
  for i in range( 2, len(x)-2 ):
    di = -fx[ i+2 ] + 16*fx[ i+1 ] - 30*fx[i] + 16*fx[i-1] - fx[ i-2 ]
    di /= 12*( x[1]-x[0] )**2
    d.append(di)
  return d

def simpson(f, a, b, n):
  h = (b-a)/n
  tot = f(a) + f(b)
  # Odd Terms
  for i in range(1, n, 2):
    tot += 4*f(a + i*h)
  # Even Terms
  for i in range(2, n-1, 2):
    tot += 2*f(a + i*h)
  return tot*h/3
  

### Part i
x = np.linspace(0, 2*np.pi, 500)
fx = [ f(i) for i in x ]
gx = [ g(i) for i in x ]

fxp = [ f_prime(i) for i in x ]

plt.plot(x[2:-2:], stencil(x,gx) )
plt.plot(x, fxp)
#plt.show()

## First Derivative
error = []
# Evaluate error for different numbers of points
for i in range(10, 50):
  x = np.linspace(0, 2*np.pi, i)
  fx = [ f(i) for i in x ]
  fxp = [ f_prime(i) for i in x ]
  gxp = stencil( x, fx )
  # Evaluate RMS Error
  # Remember to shift indicies due to stencil boundaries
  diffs = [ fxp[i+2] - gxp[i] for i in range(len(fxp)-4) ]
  rmse = np.linalg.norm( diffs )/np.sqrt(len(fxp))
  error.append( rmse )

plt.close()
# Plot derivatives
plt.subplot(121)
plt.tight_layout()
plt.title('$f^\prime(x)$ and $g^\prime(x)$')
x = np.linspace(0, 2*np.pi, 500)
gx = [ g(i) for i in x ]
gxp = stencil( x, gx)
fxp = [ f_prime(i) for i in x ]
plt.plot(x[2:-2:], gxp, label='$g^\prime(x)$ Stencil')
plt.plot(x, fxp, label='$f^\prime(x)$ Analytical')
plt.legend()
# Plot Error
plt.subplot(122)
plt.plot(error)
#plt.gcf().gca().set_yscale('log')
plt.title('Error for First Derivative')
plt.xlabel('Number of values')
plt.ylabel('RMS Error')
plt.tight_layout()
plt.savefig('Problem2ia.png')
#plt.show()

## Second Derivative
error = []
# Evaluate error for different numbers of points
for i in range(10, 50):
  x = np.linspace(0, 2*np.pi, i)
  gx = [ g(i) for i in x ]
  fxp = [ f_prime(i) for i in x ]
  gxp = stencil2( x, gx )
  # Evaluate RMS Error
  # Remember to shift indicies due to stencil boundaries
  diffs = [ fxp[i+2] - gxp[i] for i in range(len(fxp)-4) ]
  rmse = np.linalg.norm( diffs )/np.sqrt(len(fxp))
  error.append( rmse )

plt.close()
# Plot derivatives
plt.subplot(121)
plt.tight_layout()
plt.title('$f^{\prime\prime}(x)$ and $g^{\prime\prime}(x)$')
x = np.linspace(0, 2*np.pi, 500)
gx = [ g(i) for i in x ]
gxp = stencil2( x, gx)
fxp = [ f_prime2(i) for i in x ]
plt.plot(x[2:-2:], gxp, label='$g^{\prime\prime}(x)$ Stencil')
plt.plot(x, fxp, label='$f^{\prime\prime}(x)$ Analytical')
plt.legend()
# Plot Error
plt.subplot(122)
plt.plot(error)
plt.title('Error for Second Derivative')
plt.xlabel('Number of values')
plt.ylabel('RMS Error')
plt.savefig('Problem2ib.png')
#plt.show()

### Part ii
# The known area of the curve
area = F(np.pi) - F(0)
error = []
for i in range(4,100):
   error.append( abs( area - simpson( g, 0, np.pi, i ) ) )

plt.close()
plt.plot(error)
plt.gcf().gca().set_yscale('log')
plt.title('Absolute Error Using Simpsons Rule')
plt.xlabel('Number of values')
plt.ylabel('Absolute Error')
plt.savefig('Problem2ii.png')

plt.show()
