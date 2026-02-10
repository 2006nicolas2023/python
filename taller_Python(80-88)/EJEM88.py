# Vectores iniciales
codigos = [101, 102, 103]
pendientes = [5, 3, 7]
montos_pagare = [1000, 1500, 800]  # valor de cada pagaré por cliente

# Nuevos vectores
cancelados = [0, 0, 0]
pagado_mes = [0, 0, 0]

# Registrar cancelación
codigo = int(input("Código del cliente: "))
cantidad = int(input("Cantidad de pagarés a cancelar: "))

existe = False

for i in range(len(codigos)):
    if codigos[i] == codigo:
        existe = True

        if cantidad <= pendientes[i]:
            pendientes[i] -= cantidad
            cancelados[i] = cantidad
            pagado_mes[i] = cantidad * montos_pagare[i]
        else:
            print("Cantidad mayor a pagarés pendientes")
        break

if not existe:
    print("El cliente no existe")

# Listado ordenado por monto pagado (de mayor a menor)
print("\nLISTADO DE CLIENTES QUE CANCELARON PAGARÉS\n")

for i in range(len(codigos)):
    for j in range(i + 1, len(codigos)):
        if pagado_mes[j] > pagado_mes[i]:
            pagado_mes[i], pagado_mes[j] = pagado_mes[j], pagado_mes[i]
            codigos[i], codigos[j] = codigos[j], codigos[i]
            pendientes[i], pendientes[j] = pendientes[j], pendientes[i]
            cancelados[i], cancelados[j] = cancelados[j], cancelados[i]

for i in range(len(codigos)):
    if cancelados[i] > 0:
        print("Código:", codigos[i])
        print("Pagarés pendientes:", pendientes[i])
        print("Pagarés cancelados:", cancelados[i])
        print("Monto pagado:", pagado_mes[i])
        print("----------------------")

#Código del cliente: 102
#Cantidad de pagarés a cancelar: 2

#LISTADO DE CLIENTES QUE CANCELARON PAGARÉS

#Código: 102
#Pagarés pendientes: 1
#Pagarés cancelados: 2
#Monto pagado: 3000
#----------------------
