sucursales = int(input("Sucursales: "))
cumplieron = 0

for i in range(sucursales):
    codigo = input("Código sucursal: ")
    esperado = float(input("Venta esperada: "))
    venta = float(input("Venta real: "))

    if venta >= esperado:
        cumplieron += 1

    print("Sucursal", codigo, "Vendió:", venta)

print("Porcentaje que cumplieron:", (cumplieron/sucursales)*100)


#Ventas: 3
#Monto venta: 100
#Monto venta: 200
#Monto venta: 300
#Total vendido: 600.0
