import numpy as np

# https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.poly1d.html

for i in range(2):
    if i == 0:
        coefficients = [float(n) for n in input().split()]
    else:
        value_at = int(input())

d = np.poly1d(coefficients)
print(d(value_at))