import matplotlib.pyplot as plt
import numpy as np
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
  diffs.append(abs(f(x)))
  itr.append(len(diffs))
  if(abs(f(x)) < thresh or max_steps <= 0):
    return x, itr, diffs
  else:   # Recursion might not be the best idea...
    return x_next(x, f, thresh, max_steps - 1, itr, diffs)

print('Using 1D Newton-Raphson:')
W, itr, diffs = x_next(1, zeroW, 1e-10, 100, [],[])
print('W',W)
print('V',V(W))

# The function we want to find the root of
r = range(300, 3000)
x = [ i/1000 for i in r ]
fx = [ zeroW(i/1000) for i in r ]
plt.plot(x, fx)
#plt.gca().set_yscale('log')
plt.grid()
#plt.show()
plt.plot(itr,diffs)
plt.title('Convergence of W(V)',fontsize=24)
plt.xlabel('Steps',fontsize=22)
plt.ylabel(r'$log(|f(x)|)$',fontsize=22)
plt.gca().set_yscale('log')
#plt.savefig('Problem8a.png')
#plt.show()


## 2d

def f1(V,W):
  return V*(B+W)**2 - S*(B+2*W)/(W**2)-Q

def f2(V,W):
  return (-B/2*(1+V)+S/(2*W**2)-W+1/2*((1-V)*W-D*math.sqrt(1-V))-N)

# Evaluate jacobian for all four elements
def J11(V,W):
  return (B+W)**2

def J12(V,W):
  print(W)
  return (2*(B+W)*(S+V*(W**3)))/(W**3)

def J21(V,W):
  return  0.25*(-2*B+D/math.sqrt(1-V) - 2*W)

def J22(V,W):
  return (-S/(W**3)-V/2-1/2)

def NR2d(V, W):
  for i in range(100):
    # Calculate Jacobian
    print('V: ', V, '  W: ',W)
    if(W==0): break;
    a = J11(V,W)
    b = J12(V,W)
    c = J21(V,W)
    d = J22(V,W)
    ab = [a,b]
    cd = [c,d]
    J = np.matrix( [ ab, cd ] )
    #J = np.matrix( [ [ J11(V,W), J12(V,W) ], [ J21(V,W), J22(V,W) ] ] )
    Jinv = J.I
    x = np.matrix( [ [V], [W] ] )
    f = np.matrix( [[ f1(V,W) ],[ f2(V,W) ]] )
    x = x - Jinv*f
    V = x[0]
    W = x[1]
  print('V: ', V, '  W: ',W)

NR2d(0, 1)
