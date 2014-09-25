import matplotlib.pyplot as plt

def g1(x):
  return x/2 + 1/(x**3)

def g2(x):
  return 2*x/3 + 2/(3*x**2)

def g3(x):
  return x - 2/5*(x**4 - 2)

def fpi(x, thresh, max_step, f, itr, diffs):
  itr.append(len(itr)+1)
  x_new = f(x)
  d = x_new - x
  diffs.append(abs(d))
  #print("x_new = " + str(x_new) + "\tx_old = " \
  #  + str(x) + "\tdiff = " + str(d))
  if( max_step <= 0 or abs(d) < thresh):
    print( "step = "+str(100 - max_step)+"\tx_new = "+str(x_new))
    return x, itr, diffs
  else:
    return fpi(x_new, thresh, max_step-1, f, itr, diffs)

print("g1(x):")
x, itr, diffs = fpi(1, 1e-10, 900, g1, [], [])


plt.plot(itr, diffs)
plt.gca().set_yscale('log')
plt.grid()
plt.title('FPI Convergence for g1(x)')
plt.ylabel('log( |f(x_n)| )')
plt.xlabel('step, n')
#plt.savefig('Problem4da.png')
plt.show()

print("g2(x):")
x, itr, diffs = fpi(1, 10e-10, 100, g2, [], [])
plt.plot(itr, diffs)
plt.gca().set_yscale('log')
plt.grid()
plt.title('FPI Convergence for g2(x)')
plt.ylabel('log( |f(x_n)| )')
plt.xlabel('step, n')
#plt.savefig('Problem4db.png')
plt.show()

print("g2(x):")
x, itr, diffs = fpi(1, 10e-10, 100, g3, [], [])

plt.plot(itr, diffs)
plt.gca().set_yscale('log')
plt.grid()
plt.title('FPI Convergence for g3(x)')
plt.ylabel('log( |f(x_n)| )')
plt.xlabel('step, n')
#plt.savefig('Problem4dc.png')
plt.show()

