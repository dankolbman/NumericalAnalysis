import matplotlib.pyplot as plt
import math
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)



def func1(nu, T):
  return (8*math.pi*nu**2*T)

def func2(lam, T):
  return (8*math.pi*T/(lam**4))
f = []
f.append( [ func1(i/100000,  500) for i in range(0,1000) ] )
f.append( [ func1(i/100000, 1000) for i in range(0,1000) ] )
f.append( [ func1(i/100000, 5000) for i in range(0,1000) ] )
x = [ i/100000 for i in range(0,1000) ]

plt.plot(x, f[0], label='T=500K')
plt.plot(x, f[1], label='T=1000K')
plt.plot(x, f[2], label='T=5000K')
plt.legend()
plt.ylabel(r'$\frac{dU}{d\nu}\frac{c^3}{k_B}$', fontsize=22)
plt.xlabel(r'$\nu$')
plt.title(r'Rayleigh-Jeans Law ($\nu$)', fontsize=24)
plt.savefig('Problem9a.png')
#plt.show()

plt.close()


f = []
f.append( [ func2(i/100000,  500) for i in range(1,1000) ] )
f.append( [ func2(i/100000, 1000) for i in range(1,1000) ] )
f.append( [ func2(i/100000, 5000) for i in range(1,1000) ] )
x = [ i/100000 for i in range(1,1000) ]

plt.plot(x, f[0], label='T=500K')
plt.plot(x, f[1], label='T=1000K')
plt.plot(x, f[2], label='T=5000K')
plt.legend()
plt.ylabel(r'$log(\frac{dU}{d\lambda}\frac{1}{k_B})$', fontsize=22)
plt.xlabel(r'$\nu$')
plt.title(r'Rayleigh-Jeans Law ($\lambda$)', fontsize=24)
plt.gca().set_yscale('log')
plt.savefig('Problem9b.png')
#plt.show()


def func(x):
  a = 0.01997575149
  T = 1000
  return -a*(8*math.pi)*(T/1000)**3*(math.exp(x)*(x-3)+3)*x**2/((math.exp(x)-1)**2)




def secant(a, b, thresh, max_step, f):
  itr = []
  diffs = []
  x_old = a 
  x_new = b
  x_old_val = f(x_old)
  x_new_val = f(x_new)
  for i in range(max_step):
    dx = (x_old - x_new) * x_new_val / ( x_new_val - x_old_val )
    x_old = x_new
    x_old_val = x_new_val
    x_new += dx
    x_new_val = f(x_new)
    itr.append(i)
    diffs.append(abs(x_new_val))
    print('itr: ',i,'x: ', x_new, 'f(x): ', x_new_val)
    if( abs(x_new_val) < thresh):
      return x_new, itr, diffs
  return x_new, itr, diffs

#x, itr, diffs = secant(1, 10, 10e-10, 100, func)
#print(x, len(itr))

#x = [ i/100 for i in range(1,10000) ]
#fx = [ func(i/100) for i in range(1,10000) ]
plt.close()
#plt.plot(x,fx)
#plt.show()



def zerof(x):
  return (x**2*(math.exp(x)*(x-3)+3))/((math.exp(x)-1)**2)

def fun(x):
  return x**3/(math.exp(x)-1)

def fwhm(x):
  return fun(x)/fun(2.821439372122) - 0.5

# Find points for FWHM
x, itr, diffs = secant(1,3, 10e-10, 100, fwhm)
print(x, len(itr))
x, itr, diffs = secant(4,6, 10e-10, 100, fwhm)
print(x, len(itr))

x = [ i/1000 for i in range(1,10000) ]
fx = [ fwhm(i/1000) for i in range(1,10000) ]
plt.close()
plt.title(r'$u(x_h;T)-\frac{1}{2}u(x_{max};T)$', fontsize=24)
plt.plot(x,fx)
plt.savefig('Problem9d.png')
plt.show()

