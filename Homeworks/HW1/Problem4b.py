def func(x):
  return x**4 - 2

def secant(a, b, thresh, max_step, f):
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

    if( abs(x_new_val) < thresh):
      return x_new
  return x_new

print(secant(0, 2, 10e-10, 100, func))
