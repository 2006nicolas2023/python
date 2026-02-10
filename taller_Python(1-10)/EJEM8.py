import math

a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

p = (a + b + c) / 2
area = math.sqrt(p * (p - a) * (p - b) * (p - c))

print("Área del triángulo:", area)

#Se calcula p
#Luego se aplica la fórmula exacta

#----------------------------#
#Lado a: 3
#Lado b: 4
#Lado c: 5
#Área del triángulo: 6.0
