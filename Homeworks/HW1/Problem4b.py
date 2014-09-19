import matplotlib.pyplot as plt
def func(x):
  return x**4 - 2
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
    if( abs(x_new_val) < thresh):
      return x_new, itr, diffs
  return x_new, itr, diffs
x, itr, diffs = secant(0, 2, 1e-10, 100, func)

print(x)
plt.plot(itr, diffs)
plt.gca().set_yscale('log')
plt.grid()
plt.title('Secant Convergence')
plt.ylabel('log(| f(x_n) |)')
plt.xlabel('step, n')
plt.savefig('Problem4b.png')
plt.show()
