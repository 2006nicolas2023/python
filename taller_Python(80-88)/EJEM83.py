centros = int(input("Centros: "))
mayor = 0
nombre = ""

for i in range(centros):
    n = input("Nombre: ")
    r = int(input("Restaurantes: "))
    if r > mayor:
        mayor = r
        nombre = n

print("Más restaurantes:", nombre)

#Centros: 2
#Nombre: Playa
#Restaurantes: 5
#Nombre: Montaña
#Restaurantes: 8
#Más restaurantes: Montaña
