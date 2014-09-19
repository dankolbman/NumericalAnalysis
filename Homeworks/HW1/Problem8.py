import matplotlib.pyplot as plt
import math

B = 0.04
S = 0.0011111
Q = 0.083333
D = 1.29074
N = -1.774598

def V(W):
  v = Q/((B+W)**2) + S*( B+2*W )/( W**2*(B+W)**2 )
  return v

# This is the equation in terms of just W set to 0
def zeroW(W):
  #zero = math.sqrt(1-V(W))
  zero = -(B/2)*(1+V(W))+(S/(2*W**2))-W+0.5*((1-V(W))*W-D*math.sqrt(1-V(W)))-N
  return zero

def deriv(f,x): # I dont want to derive this on paper
  eps = 1e-2
  a = x - eps
  b = x + eps
  d = ( f(b)-f(a) )/( 2*eps )
  return d

def x_next(x_last, f, thresh, max_steps, itr, diffs):
  x = x_last - f(x_last)/deriv(f,x_last)
  diffs.append(x)
  itr.append(len(diffs))
  if(abs(f(x)) < thresh or max_steps <= 0):
    return x, itr, diffs
  else:   # Recursion might not be the best idea...
    return x_next(x, f, thresh, max_steps - 1, itr, diffs)

W, itr, diffs = x_next(0.31, zeroW, 1e-10, 100, [],[])
print('W',(W))
print('V',V(W))

# The function we want to find the root of
r = range(300, 3000)
x = [ i/1000 for i in r ]
fx = [ zeroW(i/1000) for i in r ]
plt.plot(x, fx)
#plt.gca().set_yscale('log')
plt.grid()
plt.show()

plt.plot(itr,diffs)
plt.show()
