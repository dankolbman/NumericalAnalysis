def func(x):
  return x**4-2

def bisection(a, b,thresh, max_step, f):
  x1 = a
  x2 = b
  
  x1_val = f(x1)
  x2_val = f(x2)
  
  # Keep x1 on the left
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

    # Get out if our guess is good enough
    if(abs(fval) < thresh):
      return mid

    # Assign midpoint
    x1 = x1 if (fval > 0) else mid
  return mid

print(bisection(0, 2, 10e-10, 100, func))
