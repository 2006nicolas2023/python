nombres = ["Maria", "Juan", "Josefina", "Jose Luis"]
notas = [
    [16,14,15,13,9],
    [10,9,7,11,14],
    [13,12,15,17,13],
    [7,11,10,8,17]
]

promedios = []

for i in range(len(nombres)):
    prom = sum(notas[i]) / len(notas[i])
    promedios.append(prom)
    print(i+1, nombres[i], prom)

prom_clase = sum(promedios) / len(promedios)

menor = mayor = 0
for p in promedios:
    if p < prom_clase:
        menor += 1
    else:
        mayor += 1

print("Promedio clase:", prom_clase)
print("Menores:", menor)
print("Mayores:", mayor)

#1 Maria 13.4
#2 Juan 10.2
#3 Josefina 14.0
#4 Jose Luis 10.6
#Promedio clase: 12.05
#Menores: 2
#Mayores: 2
