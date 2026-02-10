anterior = int(input("Lectura anterior: "))
actual = int(input("Lectura actual: "))

consumo = actual - anterior

if consumo <= 100:
    costo = consumo * 2.622
elif consumo <= 300:
    costo = consumo * 79.78
elif consumo <= 500:
    costo = consumo * 89.52
else:
    costo = consumo * 97.95

print("Consumo:", consumo)
print("Monto a pagar:", costo)

#Lectura anterior: 1200
#Lectura actual: 1400
#Consumo: 200
#Monto a pagar: 15956.0
