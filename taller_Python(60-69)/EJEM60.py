from datetime import datetime

num_fac = input("Número factura: ")
cliente = input("Nombre cliente: ")
monto = float(input("Monto factura: "))

fec_compra = input("Fecha compra (dd/mm/aaaa): ")
fec_pago = input("Fecha pago (dd/mm/aaaa): ")

f1 = datetime.strptime(fec_compra, "%d/%m/%Y")
f2 = datetime.strptime(fec_pago, "%d/%m/%Y")

dias = (f2 - f1).days

interes = 0
descuento = 0

if dias > 60:
    interes = monto * 0.08
elif 31 <= dias <= 59:
    interes = monto * 0.06
elif dias < 15:
    descuento = monto * 0.02

total = monto + interes - descuento

print("\nFactura:", num_fac)
print("Cliente:", cliente)
print("Monto base:", monto)
print("Interés mora:", interes)
print("Descuento:", descuento)
print("Monto a pagar:", total)

#Número factura: 001
#Nombre cliente: Carlos
#Monto factura: 1000
#Fecha compra (dd/mm/aaaa): 01/01/2024
#Fecha pago (dd/mm/aaaa): 10/03/2024

#Factura: 001
#Cliente: Carlos
#Monto base: 1000.0
#Interés mora: 80.0
#Descuento: 0
#Monto a pagar: 1080.0
