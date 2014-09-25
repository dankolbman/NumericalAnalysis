import math
def expand(x,thresh):
  # First term is 1
  approx = 1.0
  last_term = 1.0
  for n in range(0,100):
    new_term = last_term*3*x/(n+1)
    approx += new_term
    #print(abs(approx - math.exp(3*x)))
    #if(abs(approx - math.exp(3*x)) < thresh):
    if(abs(new_term - last_term) < thresh):
      break
    last_term = new_term
  print('terms: '+str(n), 'value: '+str(approx))
  return approx

print('Until relative error is less than 10^-15')
print('x = 2')
expand(2, 1e-9)
print('x = -2')
expand(-2, 1e-9)
print('x = -12')
expand(-12, 1e-9)
print('Until relative error is less than 10^-15')
print('x = 2')
expand(2, 1e-15)
print('x = -2')
expand(-2, 1e-15)
print('x = -12')
expand(-12, 1e-15)

print('Until relative error is less than 10^-15')
print('x = 20')
expand(20, 1e-9)
print('x = -20')
expand(-20, 1e-9)
