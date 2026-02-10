total = 0
for i in range(3):
    puntos = int(input("Puntos cuestionario: "))
    promedio = puntos / 23
    total += promedio
    print("Promedio:", promedio)

print("Promedio general:", total / 3)

#Puntos cuestionario: 80
#Promedio: 3.47
#Puntos cuestionario: 90
#Promedio: 3.91
#Puntos cuestionario: 100
#Promedio: 4.34
#Promedio general: 3.9
