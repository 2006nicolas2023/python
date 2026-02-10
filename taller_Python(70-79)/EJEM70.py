dias = 0
errores = 0
suma_max = 0
suma_min = 0

while True:
    tmax = float(input("Temperatura máxima: "))
    tmin = float(input("Temperatura mínima: "))

    if tmax == 0 and tmin == 0:
        break

    dias += 1
    suma_max += tmax
    suma_min += tmin

    if not (14 <= tmax <= 30) or not (14 <= tmin <= 30):
        errores += 1

print("Días registrados:", dias)
print("Promedio máxima:", suma_max / dias)
print("Promedio mínima:", suma_min / dias)
print("Errores:", errores)
print("Porcentaje errores:", (errores / dias) * 100)

#Temperatura máxima: 25
#Temperatura mínima: 18
#Temperatura máxima: 32
#Temperatura mínima: 10
#Temperatura máxima: 0
#Temperatura mínima: 0
#Días registrados: 2
#Promedio máxima: 28.5
#Promedio mínima: 14.0
#Errores: 1
#Porcentaje errores: 50.0
