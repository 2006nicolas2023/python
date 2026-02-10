hombres = int(input("Cantidad de hombres: "))
mujeres = int(input("Cantidad de mujeres: "))

total = hombres + mujeres

por_hombres = (hombres / total) * 100
por_mujeres = (mujeres / total) * 100

print("Porcentaje de hombres:", por_hombres)
print("Porcentaje de mujeres:", por_mujeres)

#------------------------------#
#Cantidad de hombres: 12
#Cantidad de mujeres: 18
#Porcentaje de hombres: 40.0
#Porcentaje de mujeres: 60.0
