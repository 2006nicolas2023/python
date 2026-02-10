nombre = input("Nombre del cliente: ")
monto = float(input("Monto de la compra: "))

if monto < 500:
    descuento = 0
elif monto <= 1000:
    descuento = 0.05
elif monto <= 7000:
    descuento = 0.11
elif monto <= 15000:
    descuento = 0.18
else:
    descuento = 0.25

monto_descuento = monto * descuento
total_pagar = monto - monto_descuento

print("Cliente:", nombre)
print("Monto compra:", monto)
print("Descuento:", monto_descuento)
print("Total a pagar:", total_pagar)

#Nombre del cliente: Ana
#Monto de la compra: 8000
#Cliente: Ana
#Monto compra: 8000.0
#Descuento: 1440.0
#Total a pagar: 6560.0
