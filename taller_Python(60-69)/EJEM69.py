a = int(input("Número A: "))
b = int(input("Número B: "))

suma_a = 0
suma_b = 0

for i in range(1, a):
    if a % i == 0:
        suma_a += i

for i in range(1, b):
    if b % i == 0:
        suma_b += i

if suma_a == b and suma_b == a:
    print("Son números amigos")
else:
    print("No son números amigos")

#Número A: 220
#Número B: 284
#Son números amigos
