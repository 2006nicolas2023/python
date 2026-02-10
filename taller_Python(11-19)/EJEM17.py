pvp = float(input("Precio PVP: "))
pagado = float(input("Precio pagado: "))

descuento = ((pvp - pagado) / pvp) * 100

print("Descuento aplicado:", descuento, "%")

#Precio PVP: 100000
#Precio pagado: 85000
#Descuento aplicado: 15.0 %
