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

def f1(x):
  return math.cos(2*math.pi*x)

def f2(x):
  return abs(x)/x*math.cos(2*math.pi*x)

def f3(x):
  return math.sin(2*math.pi*abs(x))

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


### cos(2pix)
x, y = [], []
n = 10
co = interp(n ,f1)
for i in range(1000):
  x.append( 2*i/1000-1 )
  yv = 0
  for j in range(n):
    yv += co[j] * math.cos( j*(math.acos( x[-1] ) ))
  y.append(yv)

plt.plot(co, label='10 Terms')

n = 20
co = interp(n ,f1)
plt.plot(co, label='20 Terms')
plt.legend(loc=3)
plt.suptitle('Chebyshev Coefficients for $f(x)=cos(2\pi x)$')
plt.savefig('Problem6ia.png')
plt.show()

n = 100
co = interp(n ,f1)
plt.suptitle('Chebyshev Coefficients for $f(x)=cos(2\pi x)$')
plt.plot(co, label='100 Terms')
plt.legend(loc=3)
plt.gca().set_yscale('log')
plt.savefig('Problem6ib.png')
plt.show()

plt.close()

### sgn cos(2pix)

n = 10
co = interp(n ,f2)
plt.plot(co, label='10 Terms')
n = 20
co = interp(n ,f2)
plt.plot(co, label='20 Terms')
plt.legend(loc=3)
plt.suptitle('Chebyshev Coefficients for $f(x)=sgn(x)cos(2\pi x)$')
plt.savefig('Problem6iia.png')
plt.show()

n = 100
co = interp(n ,f2)
plt.suptitle('Chebyshev Coefficients for $f(x)=sgn(x)cos(2\pi x)$')
plt.plot(co, label='100 Terms')
plt.legend(loc=3)
plt.gca().set_yscale('log')
plt.savefig('Problem6iib.png')
plt.show()

plt.close()

### sin(2pi|x|)

n = 10
co = interp(n ,f3)
plt.plot(co, label='10 Terms')
n = 20
co = interp(n ,f3)
plt.plot(co, label='20 Terms')
plt.legend(loc=3)
plt.suptitle('Chebyshev Coefficients for $f(x)=sin(2\pi |x|)$')
plt.savefig('Problem6iiia.png')
plt.show()

n = 100
co = interp(n ,f3)
plt.suptitle('Chebyshev Coefficients for $f(x)=sin(2\pi |x|)$')
plt.plot(co, label='100 Terms')
plt.legend(loc=3)
plt.gca().set_yscale('log')
plt.savefig('Problem6iiib.png')
plt.show()

