import matplotlib.pyplot as plt
def func(x):
  return x**4 - 2
def false_position(a, b, thresh, max_step, f):
  itr = []
  diffs = []
  x1 = a
  x2 = b
  val1 = f(x1)
  val2 = f(x2)
  # Swap values
  if( val1 > 0 ):
    x1, x2, val1, val2 = x2, x1, val2, val1
  for i in range(max_step):
    x_new = x1 + (x2 - x1)*val1/(val1 - val2)
    val_new = f(x_new)
    itr.append(i)
    diffs.append(abs(val_new))
    if( abs(val_new) < thresh):
      return x_new, itr, diffs
    if( val_new <  0 ):
      x1 = x_new
      val1 = val_new
    else:
      x2 = x_new
      val2 = val_new
  return x_new, itr, diffs
x, itr, diffs = false_position( 0, 2, 1e-10, 300, func)
print(x)
print(len(itr))
plt.plot(itr, diffs)
plt.gca().set_yscale('log')
plt.grid()
plt.title('False Position  Convergence')
plt.ylabel('log( |f(x_n)| )')
plt.xlabel('step, n')
plt.savefig('Problem4c.png')
plt.show()
