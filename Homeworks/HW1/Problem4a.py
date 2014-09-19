import matplotlib.pyplot as plt
def func(x):
  return x**4-2
def bisection(a, b,thresh, max_step, f):
  diffs = []
  itr = []
  x1 = a
  x2 = b
  x1_val = f(x1)
  x2_val = f(x2)
  if( x1_val < 0):
    x1, x2 = x1_val, x2_val
  else:
    x1, x2, = x2_val, x1_val
  dx = x2 - x1
  for i in range(max_step):
    dx /= 2
    mid = x1 + dx
    # Evaluate the midpoint
    fval = f(mid)
    itr.append(i)
    diffs.append(abs(fval))
    # Get out if our guess is good enough
    if(abs(fval) < thresh):
      return mid, itr, diffs
    # Assign midpoint
    x1 = x1 if (fval > 0) else mid
  return mid, itr, diffs
mid, itr, diffs = bisection(0, 2, 1e-10, 100, func)


plt.plot(itr, diffs)
plt.gca().set_yscale('log')
plt.grid()
plt.title('Bisection Convergence')
plt.ylabel('log( |f(x_n)| )')
plt.xlabel('step, n')
plt.savefig('Problem4a.png')
plt.show()
