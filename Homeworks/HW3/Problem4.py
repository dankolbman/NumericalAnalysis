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
  #n = 8*np.pi*(nu**4)/(c**4)/(math.exp(h*nu/(kBT))-1)
  #n = nu**2/(math.exp(nu) - 1)
  n = (np.tan(nu)/(np.cos(nu)))**2/(np.exp(np.tan(nu))-1)
  return n

def med(nu):
  #n = 8*np.pi*(nu**4)/(c**4)/(math.exp(h*nu/(kBT))-1)
  #n = nu**2/(math.exp(nu) - 1)
  n = numbers(nu)*nu
  return n

def numbersLamb(lamb):
  n = 1/(lamb**4)/(math.exp(1/lamb)-1)
  return n

def medLamb(lamb):
  return lamb*numbersLamb(lamb)

def var(nu, mean=1.09030761383):
  return (nu-mean)**2

x = np.linspace(0.01, np.pi/2-0.0001, 500)
fx = [ med(i) for i in x ]
area = simpson(numbers, 0.01, np.pi/2-0.0001, 1000)

print('Number density:', area)

median = 0.5*simpson(med, 0.01, np.pi/2-0.0001, 1000)
print('Median Energy:', median)

mean = median*2/area
print('Mean energy:',mean)

areaLamb = simpson(numbersLamb, 0.01, 10, 10000)
medianLamb = 0.5*simpson(medLamb, 0.01, 10, 10000)
meanLamb = 2*medianLamb/areaLamb
print('Mean lamb:', meanLamb)

print('c estimate:', meanLamb*mean)

v = simpson(var, 0.01, np.pi/2-0.0001, 1000)
stdev = math.sqrt(v/mean)
print('Standard Deviation:', stdev)


plt.plot(x, fx)
#plt.gcf().gca().set_yscale('log')
#plt.show()
