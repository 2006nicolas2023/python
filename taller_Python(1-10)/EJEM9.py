horas = float(input("Horas trabajadas: "))
valor_hora = float(input("Valor por hora: "))

sueldo_bruto = horas * valor_hora
descuento = sueldo_bruto * 0.20
sueldo_neto = sueldo_bruto - descuento

print("Sueldo bruto:", sueldo_bruto)
print("Descuento:", descuento)
print("Sueldo neto:", sueldo_neto)
#Primero se calcula el sueldo bruto

#----------------------#
#Horas trabajadas: 40
#Valor por hora: 5000
#Sueldo bruto: 200000.0
#Descuento: 40000.0
#Sueldo neto: 160000.0
