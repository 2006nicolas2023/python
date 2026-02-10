import math

A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))

D = B**2 - 4*A*C

if D == 0:
    x = -B / (2*A)
    print("X1 = X2 =", x)
elif D > 0:
    x1 = (-B + math.sqrt(D)) / (2*A)
    x2 = (-B - math.sqrt(D)) / (2*A)
    print("X1:", x1)
    print("X2:", x2)
else:
    print("No existen soluciones reales")

#A: 1
#B: -5
#C: 6
#X1: 3.0
#X2: 2.0
