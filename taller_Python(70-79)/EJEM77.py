estados = int(input("Estados: "))

mayor = 0
menor = 1e30
suma_total = 0

for i in range(estados):
    nombre = input("Estado: ")
    poblacion = int(input("Habitantes: "))
    suma_total += poblacion

    if poblacion > mayor:
        mayor = poblacion
        estado_mayor = nombre
    if poblacion < menor:
        menor = poblacion
        estado_menor = nombre

print("Mayor población:", estado_mayor, mayor)
print("Menor población:", estado_menor, menor)
print("Promedio habitantes:", suma_total / estados)

#Estados: 2
#Habitantes: 500000
#Habitantes: 700000
#Promedio habitantes: 600000.0
