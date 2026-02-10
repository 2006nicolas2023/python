n = int(input("Cantidad de niños: "))

tachira = capital = 0
g1 = g2 = g3 = g4 = 0
niños = niñas = 0

for i in range(n):
    sexo = input("Sexo (M/F): ")
    edad = int(input("Edad: "))
    estado = input("Estado: ")

    if estado == "Tachira":
        tachira += 1
    if estado == "Distrito Capital":
        capital += 1

    if edad < 1:
        g1 += 1
    elif edad <= 3:
        g2 += 1
    elif edad <= 6:
        g3 += 1
    else:
        g4 += 1

    if sexo == "M":
        niños += 1
    else:
        niñas += 1

print("Porcentaje Táchira:", (tachira/n)*100)
print("Porcentaje Distrito Capital:", (capital/n)*100)
print("Grupo 1:", g1, "Grupo 2:", g2, "Grupo 3:", g3, "Grupo 4:", g4)
print("Niños:", niños, "Niñas:", niñas)

#Cantidad de niños: 2
#Sexo (M/F): M
#Edad: 2
#Estado: Tachira
#Sexo (M/F): F
#Edad: 7
##Porcentaje Táchira: 50.0
#Porcentaje Distrito Capital: 50.0
#Grupo 1: 0 Grupo 2: 1 Grupo 3: 0 Grupo 4: 1
#Niños: 1 Niñas: 1
