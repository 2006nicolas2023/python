P = float(input("Precio de contado: "))
T = float(input("Valor de cada cuota: "))


precio_cuotas = T * 12
recargo = precio_cuotas - P
porcentaje = (recargo / P) * 100


print(f"Recargo: {porcentaje:.2f}%")

#Precio de contado: 1000
#Valor de cada cuota: 100
#Recargo: 20.00%