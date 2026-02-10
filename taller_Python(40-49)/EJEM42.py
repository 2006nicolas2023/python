edad = float(input("Edad (años): "))
sexo = input("Sexo (M/F): ").upper()
hemoglobina = float(input("Nivel de hemoglobina: "))

anemia = False

if edad <= 1/12:
    anemia = hemoglobina < 13
elif edad <= 0.5:
    anemia = hemoglobina < 10
elif edad <= 1:
    anemia = hemoglobina < 11
elif edad <= 5:
    anemia = hemoglobina < 11.5
elif edad <= 10:    
    anemia = hemoglobina < 12.6 
elif edad <= 15:
    anemia = hemoglobina < 13
else:
    if sexo == "F":
        anemia = hemoglobina < 12
    else:
        anemia = hemoglobina < 14

if anemia:
    print("Resultado: POSITIVO (Anemia)")
else:
    print("Resultado: NEGATIVO")

#Edad (años): 25
#Sexo (M/F): F
#Nivel de hemoglobina: 11.5
#Resultado: POSITIVO (Anemia)
