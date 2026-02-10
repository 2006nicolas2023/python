deuda = 12775
pago = 100
incremento = 125
contador = 0

while deuda > 0:
    contador += 1
    deuda -= pago
    print("Pago:", pago, "Pendiente:", max(deuda, 0))
    pago += incremento

print("Número de pagos:", contador)
print("Último pago:", pago - incremento)

#Pago: 100 Pendiente: 12675
#Pago: 225 Pendiente: 12450
#...
#Pago: 1725 Pendiente: 0
#Número de pagos: 14
#Último pago: 1725
