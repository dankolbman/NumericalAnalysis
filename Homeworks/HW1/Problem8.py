def func(x, deriv):
  f = 4*x**3 + 3*x**2 - 2*x
  d = 12*x**2 + 6*x - 2
  return d if deriv else f

def x_next(x_last, f, thresh, max_steps):
  x = x_last - f(x_last,False)/f(x_last,True)
  if(abs(f(x,False)) < thresh or max_steps <= 0):
    return x
  else:
    print("Guess " + str(max_steps) + ": " + str(x))
    return x_next(x, f, thresh, max_steps - 1)

print(x_next(1.0, func, 10e-10, 40))
