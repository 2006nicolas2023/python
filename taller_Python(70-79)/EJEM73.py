clientes = int(input("Clientes: "))

for i in range(clientes):
    codigo = input("Código cliente: ")
    nombre = input("Nombre: ")
    pagares = int(input("Cantidad pagarés: "))

    total = 0
    for j in range(pagares):
        monto = float(input("Monto pagaré: "))
        total += monto

    print("Cliente:", nombre)
    print("Pagarés:", pagares)
    print("Total adeudado:", total)
    print("-----")


#Clientes: 1
#Código cliente: 001
#Nombre: Ana
#Cantidad pagarés: 2
#Monto pagaré: 500
#Monto pagaré: 700
#Cliente: Ana
#Pagarés: 2
#Total adeudado: 1200
