import math
import matplotlib.pyplot as plt

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
font = {'family' : 'normal',
        'size'   : 24}

rc('font', **font)

pts = [ 1 , 2, 4 ]
fpts = [ math.log(i) for i in pts ]


def L3(x):
  return -math.log(2)*( (x-1)*(x-4) )/2 + math.log(4)*( (x-1)*(x-2) )/6


x = [ i/200 for i in range(1,1000) ]
fx = [ L3(i) for i in x ]

plt.plot(x, fx)
plt.plot(pts, [0, math.log(2), math.log(4) ] , 'ro',markersize=10)
plt.suptitle('Third order polynomial interpolation of $ln(x)$', fontsize=24)
plt.savefig('Problem2.png')
plt.show()

print("Actual value of ln(3):",str(math.log(3)))
print("Estimated value of ln(3):",str(L3(3)))
print("Error:",str(abs( L3(3)-math.log(3) )))

