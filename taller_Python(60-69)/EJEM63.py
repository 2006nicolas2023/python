n = int(input("Cantidad alumnos: "))

edad_m = edad_h = 0
cont_m = cont_h = 0
adultas = jovenes_h = 0
solteras_m = solteros_h = 0

for i in range(n):
    edad = int(input("Edad: "))
    sexo = input("Sexo (M/H): ")
    estado = input("Estado civil (S/C): ")

    if sexo == "M":
        edad_m += edad
        cont_m += 1
        if edad > 21:
            adultas += 1
        if estado == "S":
            solteras_m += 1
    else:
        edad_h += edad
        cont_h += 1
        if 17 < edad < 21:
            jovenes_h += 1
        if estado == "S":
            solteros_h += 1

print("Promedio edad mujeres:", edad_m/cont_m)
print("Promedio edad hombres:", edad_h/cont_h)
print("Cantidad mujeres:", cont_m)
print("Cantidad hombres:", cont_h)
print("Porcentaje mujeres adultas:", (adultas/cont_m)*100)
print("Porcentaje hombres jóvenes:", (jovenes_h/cont_h)*100)
print("Mujeres solteras:", solteras_m)
print("Hombres solteros:", solteros_h)

#Cantidad alumnos: 2
#Edad: 22
#Sexo (M/H): M
#Estado civil (S/C): S
#Edad: 19
#Sexo (M/H): H
#Estado civil (S/C): C
#Promedio edad mujeres: 22.0
#Promedio edad hombres: 19.0
#Cantidad mujeres: 1
#Cantidad hombres: 1
#Porcentaje mujeres adultas: 100.0
#Porcentaje hombres jóvenes: 100.0
#Mujeres solteras: 1
#Hombres solteros: 0
