from math import cbrt, exp, tan

var1 = int(input("Enter a number:"))

print(f'The cube root of {var1} is {cbrt(var1)}')

var2 = int(input("Enter a number:"))

print(f'The exponent of {var2} is {exp(var1)}')

var3 = int(input("Enter a number:"))

print(f'The tangent of {var3} is {tan(var1)}')

addition = cbrt(var1) + exp(var2) + tan(var3)

print(f'The sum of {cbrt(var1)}, {exp(var2)}, {tan(var3)} is {addition}')