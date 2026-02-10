monto = float(input("Monto total de la compra: "))

if monto > 500000:
    propio = monto * 0.55
    banco = monto * 0.30
    credito = monto - propio - banco
else:
    propio = monto * 0.70
    banco = 0
    credito = monto * 0.30

intereses = credito * 0.20

print("Inversión propia:", propio)
print("Préstamo banco:", banco)
print("Crédito fabricante:", credito)
print("Intereses por crédito:", intereses)

#Monto total de la compra: 600000
#Inversión propia: 330000.0
#Préstamo banco: 180000.0
#Crédito fabricante: 90000.0
#Intereses por crédito: 18000.0
