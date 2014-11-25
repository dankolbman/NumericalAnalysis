import numpy as np
import matplotlib.pyplot as plt
import math
import random
import scipy.integrate as intg

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
font = {'family' : 'normal','size'   : 16}
rc('font', **font)

def romberg(n, m, f, a, b):
  if(n == 0 and m == 0):
    return (b-a)*(f(a)+f(b))/2
  elif(m == 0):
    s = 0
    h = (b-a)/(2**n)
    for k in range(1, 2**(n-1)):
      s += f(a+(2*k-1)*h)
    return romberg(n-1, 0,f,a,b)/2 + s*h
  else:
    return romberg(n,m-1,f,a,b) + 1/(4**m-1)*(romberg(n,m-1,f,a,b)-romberg(n-1,m-1,f,a,b))

def co(x):
  return math.cos(x)**2

def lnx(x):
  return x*np.log(x+1)

def trig(x):
  return math.sin(x)**2 - 2*x*math.sin(x)+1

def invln(x):
  return 1/(x*math.log(x))

def fun(x):
  return x

print('cos(x)^2:')
print('exact:', intg.romberg(co, -1, 1) )
print('R(3,3):', romberg(3,3, co, -1, 1))

print('xln(x+1):')
print('exact:', intg.romberg(lnx, -0.75, 0.75) )
print('R(3,3):', romberg(3,3, lnx, -0.75, 0.75))

print('Trig thing:')
print('exact:', intg.romberg(trig, 1, 4))
print('R(3,3):', romberg(3,3, trig, 1, 4))

print('1/(xlnx):')
print('exact:', intg.romberg(invln, np.e, 2*np.e))
print('R(3,3):', romberg(3,3, invln, np.e, 2*np.e))
