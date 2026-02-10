X = int(input("Ingrese cantidad de naranjas: "))
Y = float(input("Precio por docena: "))
K = float(input("Ingreso total obtenido: "))


costo = (X / 12) * Y
ganancia = K - costo
porcentaje = (ganancia / costo) * 100


print(f"Porcentaje de ganancia: {porcentaje:.0f}%")

#Ingrese cantidad de naranjas: 48000
#Precio por docena: 6
#Ingreso total obtenido: 42000
#Porcentaje de ganancia: 75%