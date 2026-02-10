ext = [50, 70, 90]
precio = [500, 700, 900]

busca_ext = int(input("Superficie: "))
busca_precio = int(input("Precio: "))

if busca_ext in ext and busca_precio in precio:
    i = ext.index(busca_ext)
    del ext[i]
    del precio[i]
    print("Departamento rentado")

#Superficie: 70
#Precio: 700
#Departamento rentado
