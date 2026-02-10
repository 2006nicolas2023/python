horas_normales = float(input("Horas normales: "))
pago_hora = float(input("Pago por hora: "))
horas_extra = float(input("Horas extra: "))
hijos = int(input("Número de hijos: "))

extra = horas_extra * pago_hora * 1.25
sueldo_base = horas_normales * pago_hora
asignaciones = 25000 + (17300 * hijos) + 18000

deducciones = sueldo_base * (0.05 + 0.02 + 0.07)
sueldo_neto = sueldo_base + extra + asignaciones - deducciones

print("Sueldo neto:", sueldo_neto)

#Horas normales: 40
#Pago por hora: 5000
#Horas extra: 5
#Número de hijos: 2
# Sueldo neto: 345750.0
