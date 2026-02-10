A = int(input("Ingrese A: "))
B = int(input("Ingrese B: "))
C = int(input("Ingrese C: "))
D = int(input("Ingrese D: "))

if D == 0:
    resultado = (A - C) ** 2
else:
    resultado = (A - B) ** 3 / D

print("Resultado:", resultado)

#Ingrese A: 5
#Ingrese B: 2
#Ingrese C: 1
#Ingrese D: 3
#Resultado: 9.0
