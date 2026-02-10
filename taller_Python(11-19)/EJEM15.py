anterior = float(input("Lectura anterior: "))
actual = float(input("Lectura actual: "))
costo = float(input("Costo por kWh: "))

consumo = actual - anterior
total = consumo * costo

print("Total a pagar:", total)


#Lectura anterior: 1200
#Lectura actual: 1350
#Costo por kWh: 80
#Total a pagar: 12000.0
