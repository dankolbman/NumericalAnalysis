import math
a = 25.0
print("Squaring a square-root:")
while ( math.sqrt(a)**2 == a ):
  print('sqrt(a)^2 = ' + str(a) + ' = ' + str(math.sqrt(a)**2))
  a *= 10
# There was a rounding error
print('sqrt(a)^2 = ' + str(a) + ' != ' + str(math.sqrt(a)**2))
# Determine the exponent of the float
expo = math.floor(math.log10(a))-1.0
# Reduce to only significant digits
b = a/(10**expo)
print("Ajusting decimal placement before taking the square-root:")
print('sqrt(a)^2 = ' + str(a) + ' = ' + str((math.sqrt(b)**2)*10**expo))
