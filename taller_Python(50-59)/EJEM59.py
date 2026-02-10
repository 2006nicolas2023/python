alumnos = int(input("Cantidad de alumnos: "))

menor_prog = 999
suma_prog = 0
no_ingles = 0
aprobados = 0
reprob_mate = 0

for i in range(alumnos):
    mate = float(input("Matemática: "))
    prog = float(input("Programación: "))
    ingles = float(input("Inglés (0 si no presentó): "))

    suma_prog += prog

    if prog < menor_prog:
        menor_prog = prog

    if ingles == 0:
        no_ingles += 1

    if mate >= 10 and prog >= 10 and ingles >= 10:
        aprobados += 1

    if mate < 10:
        reprob_mate += 1

print("Menor nota programación:", menor_prog)
print("Porcentaje no presentaron inglés:", (no_ingles/alumnos)*100)
print("Aprobaron todo:", aprobados)
print("Promedio programación:", suma_prog/alumnos)
print("Porcentaje reprobados matemática:", (reprob_mate/alumnos)*100)

#Cantidad de alumnos: 2
#Matemática: 12
#Programación: 14
#Inglés (0 si no presentó): 10
#Matemática: 8
#Programación: 9
#Inglés (0 si no presentó): 0
#Menor nota programación: 9
#Porcentaje no presentaron inglés: 50.0
#Aprobaron todo: 1
#Promedio programación: 11.5
#Porcentaje reprobados matemática: 50.0
