vendedores = int(input("Vendedores: "))
com_tienda = com_calle = 0

for i in range(vendedores):
    codigo = input("Código vendedor: ")
    tipo = codigo[:2]
    monto = float(input("Monto vendido: "))

    if tipo == "11":
        com_tienda += monto * 0.10
    else:
        com_calle += monto * 0.15

print("Comisión tienda:", com_tienda)
print("Comisión calle:", com_calle)


#Vendedores: 2
#Código vendedor: 11001
#Monto vendido: 1000
#Código vendedor: 12001
#Monto vendido: 2000
#Comisión tienda: 100.0
#Comisión calle: 300.0
