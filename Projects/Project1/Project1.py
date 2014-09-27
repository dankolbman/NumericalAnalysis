import matplotlib.pyplot as plt

# Eq 1 set to 0
def eq1(x, M, k, eta, xi):
  s = 0
  for j in range(M):
    if(1+k[j]*x != 0):
      s += k[j]*eta[j]/(1+k[j]*x)
  return x*(1+s) - xi

# Macro to eq1 for specific params
def param0(x):
  return eq1(x, 1, [1], [1], 3)

def param1(x):
  return eq1(x, 1, [1], [10], 1)

def param2(x):
  return eq1(x, 3, [1,2,6], [2,3,1], 9)

def test1(x):
  return eq1(x, 1, [1], [10], 1)

def test2(x):
  return eq1(x, 2, [5,3], [4,2], 5)

def test3(x):
  return eq1(x, 3, [1,2,6], [2,3,1], 9)

################################################################################
## Plot the the curve as asked
x = [ i/100 for i in range(0, 500) ]
y = [ param0(i) for i in x ]

plt.axhline(color='black')
plt.axvline(color='black')
plt.xlabel('x')
plt.ylabel('f(x)')
#plt.ylim([-100, 100])
#plt.xlim([-0.5, 5])
plt.plot(x,y)
#plt.savefig('plot1.png')
#plt.show()

################################################################################
## Bisection

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

print('Bisection')
mid, itr, diffs = bisection( 0, 5, 1e-10, 100, param0)
print('x estimate using bisection for first set of params:')
print('x=',mid,'\tItr:',len(itr))
mid, itr, diffs = bisection( 0, 5, 1e-10, 100, param1)
print('x estimate using bisection for first set of params:')
print('x=',mid,'\tItr:',len(itr))
mid, itr, diffs = bisection( 0, 5, 1e-10, 100, param2)
print('x estimate using bisection for first set of params:')
print('x=',mid,'\tItr:',len(itr))

plt.close()
fig = plt.gcf()
print('Bisection TEST CASES -------------------')
mid, itr, diffs = bisection( 0, 2, 1e-10, 100, test1)
print(mid)
fig.add_subplot(131)
plt.plot(itr,diffs)
plt.title('Test Case 1')
plt.ylabel('Error')
plt.gca().set_yscale('log')

mid, itr, diffs = bisection( 0, 4, 1e-10, 100, test2)
print(mid)
fig.add_subplot(132)
plt.plot(itr,diffs)
plt.title('Test Case 2')
plt.gca().set_yscale('log')

mid, itr, diffs = bisection( 0, 5, 1e-10, 100, test3)
print(mid)
fig.add_subplot(133)
plt.plot(itr,diffs)
plt.title('Test Case 3')
plt.suptitle('Convergence for Bisection',fontsize=22)
plt.gca().set_yscale('log')
plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.savefig('bisect_tests.png')
#plt.show()

################################################################################
## FPI

def func2(x):
  #return x*(1+1/(1+x)) - 3
  return 3 - x/(1+x)
def func3(x):
  return 3 - 5*x/(1+x)
def func4(x,a=1):
  return 1/(1+a)*(3+x*(a-5/(1+x)))

def ga1(x,a=1):
  return 1/(1+a)*(3+x*(a-(5/(1+x))))

def ga2(x,a=1):
  return 1/(1+a)*(5+x*(a-(20/(1+5*x)+6/(1+3*x))))

def ga3(x,a=2):
  return 1/(1+a)*(9+x*(a - (1+2/(1+x)+2*3/(1+2*x) + 6/(1+6*x))))



def fpi(x, thresh, max_step, f):
  itr = []
  diffs = []
  for i in range(max_step):
    itr.append(i)
    x_new = f(x)
    d = x_new - x
    diffs.append(abs(d))
    x = x_new
    if(abs(d) < thresh):
      return x, itr, diffs
  return x, itr, diffs

print('FPI')
print('first form (works}')
x, itr, diffs = fpi(3, 1e-10, 100, func2)
print(x)
print('Second form (doesnt work)')
x, itr, diffs = fpi(3, 1e-10, 100, func3)
print(x)
print('Third form (does work?)')
x, itr, diffs = fpi(3, 1e-10, 100, func4)
print(x)

plt.close()
fig = plt.gcf()
print('FPI TEST CASES -------------------')
x, itr, diffs = fpi(1, 1e-11, 100, ga1)
print(x)
fig.add_subplot(131)
plt.plot(itr,diffs)
plt.title('Test Case 1')
plt.ylabel('Error')
plt.gca().set_yscale('log')

x, itr, diffs = fpi(1, 1e-11, 100, ga2)
print(x)
fig.add_subplot(132)
plt.plot(itr,diffs)
plt.title('Test Case 2')
plt.gca().set_yscale('log')

x, itr, diffs = fpi(4, 1e-11, 100, ga3)
print(x)
fig.add_subplot(133)
plt.plot(itr,diffs)
plt.title('Test Case 3')
plt.gca().set_yscale('log')
plt.suptitle('Convergence for FPI',fontsize=22)
plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.savefig('fpi_tests.png')
#plt.show()



x = [ i/100 for i in range(0, 500) ]
y1 = [ func2(i) for i in x ]
y2 = [ func3(i) for i in x ]

plt.xlabel('x')
plt.ylabel('f(x)')
#plt.ylim([-100, 100])
#plt.xlim([-0.5, 5])
#plt.plot(itr, diffs)
#plt.savefig('plot1.png')
#plt.show()


################################################################################
### Newton's Method


def deriv(f,x):
  eps = 1e-10
  a = x - eps
  b = x + eps
  d = ( f(b)-f(a) )/( 2*eps )
  return d

def deriv2(x):
  return x**2+2*x+11/((x+1)**2)

def x_next(x_last, f, thresh, max_steps, itr, diffs):
  x = x_last - f(x_last)/deriv(f,x_last)
  diffs.append(abs(f(x)))
  itr.append(len(diffs))
  #print('itr',max_steps,'\tx',x)
  if(abs(f(x)) < thresh or max_steps <= 0):
    return x, itr, diffs
  else:
    return x_next(x, f, thresh, max_steps - 1, itr, diffs)

print("Init guess x = 1.6")
x, itr, diffs = x_next( 1.6, param1, 1e-14, 100, [], [])
#plt.plot(itr,diffs)
#plt.gca().set_yscale('log')
#plt.show()
print(x)
print("Init guess x = 1.4999")
x, itr, diffs = x_next( 1.4999, param1, 1e-14, 100, [], [])
#plt.plot(itr,diffs)
#plt.gca().set_yscale('log')
#plt.show()
print(x)
print("Init guess x = 1.5")
x, itr, diffs = x_next( 1.5, param1, 1e-14, 100, [], [])
#plt.plot(itr,diffs)
#plt.gca().set_yscale('log')
#plt.show()
print(x)
print("Init guess x = 1.0")
x, itr, diffs = x_next( 1.0, param1, 1e-14, 100, [], [])
#plt.plot(itr,diffs)
#plt.gca().set_yscale('log')
#plt.show()
print(x)

# Final set of params given
print("------------")
x, itr, diffs = x_next( -0.2, param2, 1e-14, 100, [], [])
plt.close()
fig = plt.gcf()
print('NEWTON TEST CASES -------------------')
x, itr, diffs = x_next( 0.0, test1, 1e-11, 100, [], [])
print(x)
fig.add_subplot(131)
plt.plot(itr,diffs)
plt.title('Test Case 1')
plt.ylabel('Error')
plt.gca().set_yscale('log')

x, itr, diffs = x_next( 1.0, test2, 1e-11, 100, [], [])
print(x)
fig.add_subplot(132)
plt.plot(itr,diffs)
plt.title('Test Case 2')
plt.gca().set_yscale('log')

x, itr, diffs = x_next( 3.0, test3, 1e-11, 100, [], [])
print(x)
fig.add_subplot(133)
plt.plot(itr,diffs)
plt.title('Test Case 3')
plt.suptitle('Convergence for Newton\s Method',fontsize=22)
plt.gca().set_yscale('log')
plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.savefig('newton_tests.png')
#plt.show()
