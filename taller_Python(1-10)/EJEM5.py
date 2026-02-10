parciales = []

for i in range(3):
    nota = float(input(f"Ingrese parcial {i+1}: "))
    parciales.append(nota)

examen_final = float(input("Nota del examen final: "))
trabajo_final = float(input("Nota del trabajo final: "))

prom_parciales = round(sum(parciales) / 3, 2)

nota_final = (prom_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

nota_final = round(nota_final, 2)

print("Nota final:", nota_final)



#Cada parte pesa un porcentaje
#Todo se suma al final


#----------------------------#
#Ingrese parcial 1: 4.0
#Ingrese parcial 2: 3.5
#Ingrese parcial 3: 4.2
#Nota del examen final: 4.5
#Nota del trabajo final: 4.0
#Nota final: 4.12
