import matplotlib.pyplot as plt
import math
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)



def func(nu, T):
  return (8*math.pi*nu**2*T)

f = []
f.append( [ func(i/100,  500) for i in range(-100,100) ] )
f.append( [ func(i/100, 1000) for i in range(-100,100) ] )
f.append( [ func(i/100, 2000) for i in range(-100,100) ] )
x = [ i/100 for i in range(-100,100) ]

plt.plot(x, f[0], label='T=500K')
plt.plot(x, f[1], label='T=1000K')
plt.plot(x, f[2], label='T=2000K')
plt.legend()
plt.ylabel(r'$\frac{dU}{d\nu}\frac{c^3}{k_b}$', fontsize=22)
plt.xlabel(r'$\nu$')
plt.title(r'Rayleigh-Jeans Law ($\nu$)', fontsize=24)
plt.savefig('Problem9a.png')
plt.show()



