import math

valor1 = float(input("Valor 1: "))
valor2 = float(input("Valor 2: "))
area = float(input("Área a comparar: "))

area_triangulo = (valor1 * valor2) / 2
area_rectangulo = valor1 * valor2
area_circulo = math.pi * (valor1 ** 2)

if abs(area_triangulo - area) < 0.01:
    print("La figura es un TRIÁNGULO")
elif abs(area_rectangulo - area) < 0.01:
    print("La figura es un RECTÁNGULO")
elif abs(area_circulo - area) < 0.01:
    print("La figura es un CÍRCULO")
else:
    print("No corresponde a ninguna figura")

#Valor 1: 10
#Valor 2: 5
#Área a comparar: 25
#La figura es un TRIÁNGULO
