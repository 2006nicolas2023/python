G = 6.67259e-11
M = 5.97e24

n = int(input("Cantidad satélites: "))

mayor_f = 0
menor_f = 1e30
suma_f = 0
mayor_masa = 0
suma_masa = 0
menor_altura = 1e30
mayor_altura = 0

for i in range(n):
    masa = float(input("Masa: "))
    altura = float(input("Altura: "))

    F = G * masa * M / (altura**2)

    suma_f += F
    suma_masa += masa

    if F > mayor_f:
        mayor_f = F
    if F < menor_f:
        menor_f = F
    if masa > mayor_masa:
        mayor_masa = masa
    if altura < menor_altura:
        menor_altura = altura
    if altura > mayor_altura:
        mayor_altura = altura

print("Mayor fuerza:", mayor_f)
print("Menor fuerza:", menor_f)
print("Fuerza promedio:", suma_f / n)
print("Mayor masa:", mayor_masa)
print("Masa promedio:", suma_masa / n)
print("Menor altura:", menor_altura)
print("Mayor altura:", mayor_altura)

#Cantidad satélites: 2
#Masa: 8300
#Altura: 31200000
#Masa: 5500
#Altura: 36000000
#Mayor fuerza: 3.39
#Menor fuerza: 1.69
