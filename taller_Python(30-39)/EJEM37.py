import math

a = int(input("Lado A: "))
b = int(input("Lado B: "))
c = int(input("Lado C: "))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    if a == b == c:
        tipo = "Equilátero"
    elif a == b or a == c or b == c:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"

    print("Tipo:", tipo)
    print("Área:", area)
else:
    print("No es un triángulo")

#Lado A: 3
#Lado B: 4
#Lado C: 5
#Tipo: Escaleno
#Área: 6.0
