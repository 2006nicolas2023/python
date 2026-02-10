sueldo_base = float(input("Ingrese el sueldo base: "))

ventas = []
for i in range(3):
    venta = float(input(f"Ingrese el valor de la venta {i+1}: "))
    ventas.append(venta)

comisiones = sum(ventas) * 0.10
total = sueldo_base + comisiones

print("Comisiones:", comisiones)
print("Total a recibir:", total)

#Se suman todas las ventas
#Se calcula el 10%
#Se suma al sueldo base

#------------------------------------#
#Ingrese el sueldo base: 120000
#Ingrese el valor de la venta 1: 50000
#Ingrese el valor de la venta 2: 30000
#Ingrese el valor de la venta 3: 20000
#Comisiones: 10000.0
#Total a recibir: 130000.0
