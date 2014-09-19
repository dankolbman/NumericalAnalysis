import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

def omega(x,k, A, B, C):
  return (k)/(A*x**2+B*x+C)

x = [ i/2000 for i in range(0,1000) ]
fx1 = [ (omega(i/2000, 1, 1, 1.5, -0.25) - omega(i/2000, 1, 4, -6.4, 1.5)) \
      for i in range(0,1000) ]
fx2 = [ 1/(omega(i/2000, 1, 1, 1.5, -0.25) - omega(i/2000, 1, 4, -6.4, 1.5)) \
      for i in range(0,1000) ]

plt.plot(x,fx1, label=r'\Omega_1-\Omega_2')
plt.plot(x, fx2, label=r'(\Omega_1-\Omega_2)^{-1}')
plt.ylabel(r'\Omega_1 - \Omega_2', fontsize=24)
plt.xlabel(r'x', fontsize=24)
plt.grid()
plt.legend()
plt.ylim([-100, 100])
plt.savefig('Problem6a.png')
plt.show()
