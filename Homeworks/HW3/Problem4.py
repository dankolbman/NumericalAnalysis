import numpy as np
import matplotlib.pyplot as plt
import math
import random

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
font = {'family' : 'normal','size'   : 24}
rc('font', **font)

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

def numbers(nu):
  kBT = 1
  h = 1
  c = 1
  n = 8*np.pi*(nu**4)/(c**4)/(math.exp(h*nu/(kBT))-1)
  return n
  

x = np.linspace(0, 20, 500)
fx = [ numbers(i) for i in x ]
area = simpson(numbers, 0.01, 25, 1000)

print('Number density:',area)

#plt.plot(x, fx)
#plt.gcf().gca().set_yscale('log')
#plt.show()
