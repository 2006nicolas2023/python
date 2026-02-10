g = int(input("Grupos: "))

for i in range(g):
    n = int(input("Alumnos grupo: "))
    suma_grupo = 0

    for j in range(n):
        suma_mat = 0
        for k in range(3):
            suma_mat += float(input("Nota: "))
        prom_alumno = suma_mat / 3
        suma_grupo += prom_alumno

    print("Promedio grupo:", suma_grupo / n)


#Alumnos: 2
#Promedio alumno: 4
#Promedio alumno: 3
#Promedio grupo: 3.5
