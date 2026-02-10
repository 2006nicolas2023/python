pasajeros = int(input("Cantidad pasajeros: "))
no_pagan = 0
total_vuelo = 0

for i in range(pasajeros):
    vuelo = input("Número vuelo: ")
    nombre = input("Nombre pasajero: ")
    peso = float(input("Peso equipaje: "))

    if peso <= 3:
        pago = 0
        no_pagan += 1
    elif peso <= 6:
        pago = 600
    elif peso <= 9:
        pago = 1200
    elif peso <= 12:
        pago = 1500
    elif peso <= 15:
        pago = 2000
    else:
        pago = 2500

    total_vuelo += pago

    print("Vuelo:", vuelo)
    print("Pasajero:", nombre)
    print("Peso total:", peso)
    print("Monto a pagar:", pago)
    print("------")

print("Total recaudado vuelo:", total_vuelo)
print("Porcentaje que no pagó:", (no_pagan/pasajeros)*100)

#Cantidad pasajeros: 2
#Número vuelo: AV01
#Nombre pasajero: Ana
#peso equipaje: 2
#Monto a pagar: 0
#------
#Número vuelo: AV01
#Nombre pasajero: Juan
#Peso equipaje: 10
#Monto a pagar: 1500
#------
#Total recaudado vuelo: 1500
#Porcentaje que no pagó: 50.0
