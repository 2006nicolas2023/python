horas = int(input("Horas trabajadas: "))
tipo = int(input("Tipo empleado (1,2,3): "))

if tipo == 1:
    pago = 5000
elif tipo == 2:
    pago = 10000
else:
    pago = 15000

sueldo = horas * pago
seguro = sueldo * 0.03 if sueldo > 100000 else 0

print("Sueldo básico:", sueldo)
print("Seguro social:", seguro)

#Horas trabajadas: 10
#Tipo empleado (1,2,3): 2
#Sueldo básico: 100000
#Seguro social: 0
