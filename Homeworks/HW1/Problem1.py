"""Problem 1: Break math
Break math using a computer. To be a bit more specific, demonstrate a
numerical calculation using the computer language of your choice where
the answer is demonstrably wrong. I'll want to see the code you used,
preferably something brief and punchy, and then the result. For full credit,
fix math again by demonstrating an alternate method of calculating the
result that previously broke math but yields the correct answer
"""
import math

a = 25.0
while ( math.sqrt(a)**2 == a ):
  print('sqrt(a)^2 = ' + str(a) + ' = ' + str(math.sqrt(a)**2))
  a *= 10
# There was a rounding error
print('sqrt(a)^2 = ' + str(a) + ' != ' + str(math.sqrt(a)**2))
# Determine the exponent of the float
expo = math.floor(math.log10(a))-1.0
# Reduce to only significant digits
b = a/(10**expo)
print('sqrt(a)^2 = ' + str(a) + ' = ' + str((math.sqrt(b)**2)*10**exp))
