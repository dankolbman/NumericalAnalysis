import numpy as np
import matplotlib.pyplot as plt
import math
import random
from scipy import stats
import scipy.integrate as sp

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
font = {'family' : 'normal','size'   : 32}
rc('font', **font)

# Differential Equations

# Steps the y function usig euler
def y0_step(y0, y1, t, dt, n):
  return y0 + y1*dt

# Steps y` using euler
def y1_step(y0, y1, t, dt, n):
  return y1 + (-2/t*y1-y0**n)*dt


def euler2( a, b, steps, y0, y1, y0_step, y1_step, n=1):
  #t = np.linspace(a, b, steps)
  t = [a]
  # Function values
  y0_vals = [y0]
  # Derivative values
  y1_vals = [y1]
  dt = (b-a)/steps

  # Integrate
  for i in range(steps):
    # Next time to evaluate
    t.append( t[-1] + dt )
    # Step derivative
    y1_vals.append( y1_step( y0_vals[-1], y1_vals[-1], t[i], dt, n) )
    # Step the function
    y0_vals.append( y0_step( y0_vals[-1], y1_vals[-1], t[i], dt, n) )
    if( y0_vals[-1] < 0.0):
      break
  plt.plot(t, y0_vals, label='$n = '+str(n)+'$', lw=9, alpha=0.6)
  return t, y0_vals, y1_vals

# Determine dimensionless mass
def mass(xi, thet, n=1):
  s = 0.0
  dxi = xi[1]-xi[0]
  for i in range(len(thet)):
    if(n == 1):
      s += thet[i]*xi[i]**2*dxi
    elif(thet[i] > 0.0):
      s += math.pow(thet[i], n ) * xi[i]**2*dxi
  s *= 4*np.pi
  return s

# Determine dimensionless intensity
def intensity(xi, thet, m):
  s = 0.0
  dxi = xi[1]-xi[0]
  for i in range(len(thet)):
    s += thet[i]*xi[i]**4*dxi
  s *= 8/3*np.pi
  # Dedimensionalize
  return s/(m*xi[-1]**2)

# Determine dimensionless potential energy
def potential(xi, thet, m, n):
  s = 0.0
  dxi = xi[1]-xi[0]
  for i in range(len(thet)):
    if(n == 1):
      s += thet[i]*xi[i]*dxi
    elif(thet[i] > 0.0):
      s += math.pow( thet[i], n )*xi[i]*dxi
  s *= 4*np.pi*m
  # Dedimensionalize
  return s*xi[-1]/(m**2)

# Initial values
y0 = 1
y1 = 0  

##########

# Test Euler
steps = 10000
a,b = 0.00001, 6.0

n = [ 0.5, 1.0, 2.0, 3.0 ]

ms = []
ks = []
xis = []

# Iterate models for different n's
for i in n:
  print('======================')
  print('n =', i)
  xi, thet0, thet1 = euler2( a, 7.3, steps, y0, y1, y0_step, y1_step, i )
  print('Radius:', xi[-1])
  m = mass(xi, thet0, i)
  print('Mass:', m)
  I = intensity(xi, thet0, m)
  print('Intensity:', I)
  O = potential(xi, thet0, m, i)
  print('Potential:', O)
  print('-dthet/dxi at radius:', -thet1[-1])
  ms.append(m)
  ks.append(thet1[-1])
  xis.append(xi[-1])

print('======================')
# Using n = 3
GRAV = 6.674e-8 # in cgs
# Mass of sun
msun = 1.989e33 # g
# Radius of sun
rsun = 695.8e8  # cm
# Determine alpha
alpha = rsun/xis[3]
print('Alpha:',alpha)
print('Non dimensional m:', ms[3])
# rho_c = M_sun / (alpha^3 M^hat)
rhoc = msun / (alpha**3*ms[3])
print('Rhoc:', rhoc)
kappa = alpha**2*4*np.pi*GRAV/(3+1)/(rhoc**( (1-3)/3 ) )
print('Kappa:', kappa)
Pc = kappa*rhoc**(1+1/3)

print('Central pressure of sun:', Pc)

# Look at the last endpoint to determine the error
#err = abs( f_vals[-1] - f( t[-1] ) )
#print('Err =', err)

plt.xlabel(r'$\xi$')
plt.ylabel(r'$\theta$')
plt.ylim(0.0, 1.0)
plt.legend(fontsize=22)
plt.tight_layout()
plt.savefig('lane-emden.png')
#plt.show()

plt.close()
slope, intercept = np.polyfit(ks, ms, 1)
print('K:', slope)
plt.plot( ks, ms, lw=9, )
plt.text(0.5, 0.8,\
  'K  = '+str(round(slope*10000)/10000),\
  transform = plt.gca().transAxes,fontsize=32)
plt.xlabel(r'$\Xi^2(\frac{d\theta}{d\xi})_{\xi=\Xi}$')
plt.ylabel(r'$\hat{M}$')
plt.tight_layout()
plt.savefig('K.png')
#plt.show()

plt.cla()
plt.clf()
plt.close()
print('======================')

################################################################################
#### White Dwarfs

def G(thet):
  return (thet**(-1/3)*(4*thet**(2/3)+5))/(3*(thet**(2/3)+1)**(3/2))

# Steps the y function usig euler
def y0_step(y0, y1, t, dt):
  return y0 + y1*dt

# Steps y` using euler
def y1_step(y0, y1, t, dt):
  return y1 + (-2/t*y1-y0/G(y0))*dt

def euler2( a, b, steps, y0, y1, y0_step, y1_step):
  #t = np.linspace(a, b, steps)
  t = [a]
  # Function values
  y0_vals = [y0]
  # Derivative values
  y1_vals = [y1]
  dt = (b-a)/steps

  # Integrate
  for i in range(steps):
    # Next time to evaluate
    t.append( t[-1] + dt )
    # Step derivative
    y1_vals.append( y1_step( y0_vals[-1], y1_vals[-1], t[i], dt) )
    # Step the function
    y0_vals.append( y0_step( y0_vals[-1], y1_vals[-1], t[i], dt) )
    if( y0_vals[-1] < 0.001):
      break
  return t, y0_vals, y1_vals

# Radii
rs = []
# Masses
ms = []

rho0 = 3.789e6
a = 1.557e8

for i in range(-2,6):
  plt.clf()
  s, thet0, thet1 = euler2( 0.0001, 10, 100000, 10**i, 0.0, y0_step, y1_step)
  #plt.subplot(2,4,i+3)
  plt.plot(s, thet0, lw=9, alpha=0.6)
  plt.title(r'$\theta (0) = 10^{'+str(i)+'}$')
  plt.xlabel(r's')
  plt.ylabel(r'$\theta$')
  plt.ylim(0, max(thet0)*1.01)
  plt.gca().xaxis.set_ticks( np.linspace(s[0], s[-1], 5) )
  plt.tight_layout()
  plt.savefig('white_dwarf-'+str(i+3)+'.png')
  print('======================')
  print('10 ^', i)
  print('Radius:', s[-1])
  m = mass(s, thet0)
  print('Dimensionless Mass:', m)
  rs.append(a*s[-1])
  ms.append(0.09/(4*np.pi)*m*msun)
  #plt.gca().set_yscale('log')
  #plt.gca().set_xscale('log')

#plt.show()

plt.close()
plt.plot(rs,ms, lw=9)
plt.title('Mass-Radius Relation')
plt.xlabel(r'Radius (cm)')
plt.ylabel(r'Mass (g)')
plt.gca().set_xscale('log')
plt.gca().set_yscale('log')
plt.tight_layout()
plt.savefig('massradius.png')
plt.show()
