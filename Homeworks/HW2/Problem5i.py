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

def f(t):
  return 1/(1+t**2)

# The function
x = [ i/100 for i in range(-500,500) ]
fx = [ f(i) for i in x ]
plt.plot(x,fx, label='f(t)', linewidth=3)

### 5 points
pts = np.linspace(-5, 5, 5)
fpts = [ f(t) for t in pts ]
# Interpolate with package
fit = intrp.lagrange(pts, fpts)
x = [ i/100 for i in range(-500,500) ]
fx = [ fit(i) for i in x ]
plt.plot(x,fx, 'g', label='5 Points')

diffs = [ f(i)-fit(i) for i in x ]
rmse=np.linalg.norm( diffs )/np.sqrt(len(fx))
print('Error for 5 Points:', rmse)

### 10 points
pts = np.linspace(-5, 5, 10)
fpts = [ f(t) for t in pts ]
# Interpolate with package
fit = intrp.lagrange(pts, fpts)
x = [ i/100 for i in range(-500,500) ]
fx = [ fit(i) for i in x ]
plt.plot(x,fx, 'c',label='10 Points')

diffs = [ f(i)-fit(i) for i in x ]
rmse=np.linalg.norm( diffs )/np.sqrt(len(fx))
print('Error for 10 Points:', rmse)

### 15 points
pts = np.linspace(-5, 5, 15)
fpts = [ f(t) for t in pts ]
# Interpolate with package
fit = intrp.lagrange(pts, fpts)
x = [ i/100 for i in range(-500,500) ]
fx = [ fit(i) for i in x ]
plt.plot(x,fx, 'r', label='15 Points', linewidth=2)

diffs = [ f(i)-fit(i) for i in x ]
rmse=np.linalg.norm( diffs )/np.sqrt(len(fx))
print('Error for 15 Points:', rmse)

plt.legend(fontsize=16)
plt.title('Interpolating Polynomials for $f(t)$')
plt.savefig('Problem5i.png')
plt.show()
