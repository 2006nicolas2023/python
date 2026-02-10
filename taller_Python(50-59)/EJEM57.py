n = float(input("Número: "))
x = 0.1

while True:
    r = (x + n / x) / 2
    if abs(r - x) < 0.000001:
        break
    x = r

print("Raíz:", r)

#Número: 25
#Raíz: 5.0
