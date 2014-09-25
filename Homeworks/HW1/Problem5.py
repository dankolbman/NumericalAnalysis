import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

def g1(x):
  #return x + 0.1*(1/(2*x**2-6))
  return (1/(2*x**2-6))

def g2(x):
  return 3/x+1/(2*x**2)

def g3(x):
  return (3*x+1/2)**(1/3.0)

def fpi(x, thresh, max_step, f):
  itr = []
  diffs = []
  #print("x_new = " + str(x_new) + "\tx_old = " \
  #  + str(x) + "\tdiff = " + str(d))
  for i in range(max_step):
    itr.append(i)
    x_new = f(x)
    d = x_new - x
    diffs.append(abs(d))
    x = x_new
    if(abs(d) < thresh):
      return x, itr, diffs
  return x, itr, diffs

print("g1(x):")
x, itr, diffs = fpi(-5, 1e-10, 100, g1)
print(x)


plt.plot(itr, diffs)
plt.gca().set_yscale('log')
plt.grid()
plt.title(r'FPI Convergence for $g_1(x)$', fontsize=28)
plt.ylabel('$log(|f(x_n)|)$', fontsize=24)
plt.xlabel('step, n', fontsize=24)
plt.savefig('Problem5a.png')
plt.show()

print("g2(x):")
x, itr, diffs = fpi(-1, 1e-10, 100, g2)
print(x)
plt.plot(itr, diffs)
plt.gca().set_yscale('log')
plt.grid()
plt.title(r'FPI Convergence for $g_2(x)$', fontsize=28)
plt.ylabel('$log(|f(x_n)|)$', fontsize=24)
plt.xlabel('step, n', fontsize=24)
plt.savefig('Problem5b.png')
plt.show()

print("g3(x):")
x, itr, diffs = fpi(3, 1e-10, 100, g3)
print(x)
x, itr, diffs = fpi(-0.1, 1e-10, 100, g3)
print(x)
plt.plot(itr, diffs)
plt.gca().set_yscale('log')
plt.grid()
plt.title(r'FPI Convergence for $g_3(x)$',fontsize=28)
plt.ylabel('$log(|f(x_n)|)$',fontsize=24)
plt.xlabel('step, n',fontsize=24)
plt.savefig('Problem5c.png')
plt.show()


