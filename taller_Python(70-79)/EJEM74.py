obreros = int(input("Cantidad obreros: "))
limite = int(input("Meta semanal: "))

total_general = 0
mayor = 0
nombre_mayor = ""
cumplieron = 0

for i in range(obreros):
    nombre = input("Nombre: ")
    total = 0
    for d in range(6):
        total += int(input("Producción diaria: "))

    total_general += total

    if total >= limite:
        cumplieron += 1
    if total > mayor:
        mayor = total
        nombre_mayor = nombre

    print(nombre, "produjo:", total)

print("Porcentaje que cumplieron:", (cumplieron/obreros)*100)
print("Mayor producción:", nombre_mayor, mayor)
print("Promedio semanal:", total_general/obreros)
